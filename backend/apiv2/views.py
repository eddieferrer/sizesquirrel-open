import datetime
import pickle
from urllib.parse import urlparse
from collections import Counter, defaultdict
from sqlalchemy import func, or_, cast, Float,  and_
from flask import jsonify, abort, request, g, current_app
from flask_httpauth import HTTPTokenAuth
from backend import app, db
from sentry_sdk import capture_message
from backend.models import User, User_Item, Item, Brand, convert_shoe_size_to_standards
from backend.utils import convert_shoe_size_to_inches
from backend.match.views import match_function, process_results_dict, match_by_street_shoe_size
from backend.scripts.set_stats_items import shoe_stats

token_auth = HTTPTokenAuth(scheme='Bearer')

from .admin_views import *
from .auth_views import *
from .user_views import *

@token_auth.verify_token
def verify_token(token):
    user = User.query.filter_by(token=token).first()
    if user:
        g.current_user = user
        if user.date_last_login < datetime.datetime.utcnow() - datetime.timedelta(1):
            user.date_last_login = datetime.datetime.now()
            db.session.commit()
        return user
    else:
        return False


# /apiv2/brand/

@app.route('/apiv2/brand/<brand_id>', methods=['GET'])
@app.cache.cached(timeout=14400)
def get_brand(brand_id):
    brand = Brand.query.filter_by(id=brand_id).first()
    if not brand:
        response = jsonify({
            'status': 'error',
            'message': 'Brand not found',
        })
        response.status_code = 400
        return response
    return jsonify({
        'status': 'success',
        'message': '',
        'brand': brand.serialize()
    })
# /apiv2/brands/

@app.route('/apiv2/brands/', methods=['GET'])
@app.cache.cached(timeout=14400)
def get_brands():
    brands = Brand.query.all()
    return jsonify({
        'status': 'success',
        'message': '',
        'brands': [e.serialize() for e in brands]
    })

# /apiv2/context/

@app.route('/apiv2/context/', methods=['POST'])
def get_context():
    urlParsed = urlparse(request.json.get('url'))

    urlSegments = urlParsed.path.split('/')
    urlSegments = list(filter(None, urlSegments)) 
    # print(urlSegments)

    profile_id = ''
    brand_id = ''
    model_id_list = []

    if urlSegments:
        if urlSegments[0] == 'shoes':
            # @app.route('/shoes/<shoe_brand>/<shoe_model>/')
            if len(urlSegments) > 1:
                brand_url_segment = urlSegments[1].replace('-', ' ')
                brand = Brand.query.filter_by(name=brand_url_segment).first()
                if brand: 
                    brand_id = brand.id
            if len(urlSegments) > 2:
                model_url_segment = urlSegments[2].replace('-', ' ')
                model_url_segment = model_url_segment.lower()
                model = Item.query.filter(Item.brand_id == brand_id).filter(func.replace(func.lower(Item.model), '-', ' ') == model_url_segment ).all()
                model.sort(reverse=False, key=lambda x: getattr(x, 'gender_id'))
                model_id_list = [x.id for x in model]
                
        if urlSegments[0] == 'profile':
            # @app.route('/profile/<user_username>/')
            if len(urlSegments) > 1:
                profile_url_segment = urlSegments[1].replace('-', ' ')
                user = User.query.filter(func.lower(User.username) == profile_url_segment.lower() ).first()
                if user: 
                    profile_id = user.id

    return jsonify({
        'status': 'success',
        'message': '',
        'profile_id': profile_id,
        'brand_id': brand_id,
        'model_id_list': model_id_list,
    })

# /apiv2/match/

@app.route('/apiv2/match/public/', methods=['POST'])
def post_match_public():
    want_item_id = request.json.get('wantItemId')
    size = request.json.get('size')
    have_item_id = request.json.get('haveItemId')

    if not want_item_id or not size or not have_item_id:
        response = jsonify({
            'status': 'error',
            'message': 'Invalid Request',
        })
        response.status_code = 400
        return response
    else:
        size_in = convert_shoe_size_to_inches(size)

        # get target item information
        target_item = Item.query.filter_by(id=want_item_id).first()

        results_dict = match_function(have_item_id, size_in, want_item_id)

        results = process_results_dict(results_dict)

        return jsonify({
            'status': 'success',
            'message': '',
            'target_item': target_item.serialize(),
            'match_results': sorted(results, key=lambda k: k['percentage'], reverse=True),
        })

@app.route('/apiv2/match/private/', methods=['POST'])
@token_auth.login_required
def post_match_private():
    want_item_id = request.json.get('wantItemId')

    if not want_item_id:
        response = jsonify({
            'status': 'error',
            'message': 'Invalid Request',
        })
        response.status_code = 400
        return response
    else:
        # get target item information
        target_item = Item.query.filter_by(id=want_item_id).first()

        # get list of all of searchers shoes.
        users_items = User_Item.query.filter_by(user_id=g.current_user.id).all()

        combined_results_dict = {}
        for sshoe in users_items:
            if int(sshoe.item_id) != int(want_item_id):
                results_dict = match_function(
                    sshoe.item_id, convert_shoe_size_to_inches(sshoe.size), want_item_id)
                if results_dict:
                    for user in results_dict:
                        if user in combined_results_dict:
                            combined_results_dict[user].update(results_dict[user])
                        else:
                            combined_results_dict[user] = results_dict[user]

        results = process_results_dict(combined_results_dict)

        # gets recommended sizes per model
        groups = defaultdict(list)
        for user in combined_results_dict:
            for key in combined_results_dict[user]:
                groups[combined_results_dict[user][key]['has_item_id']].append(
                    combined_results_dict[user][key])
        grouped_match_users = groups.values()

        grouped_results = []
        for gusers in grouped_match_users:
            most_common_guser_size = Counter(
                d['recommended_size_in'] for d in gusers).most_common(1)[0]
            grouped_results.append({
                'shoe': Item.query.filter_by(id=gusers[0]['has_item_id']).first().serialize(),
                'most_common_size': convert_shoe_size_to_standards(most_common_guser_size[0])
            })

        return jsonify({
            'status': 'success',
            'message': '',
            'target_item': target_item.serialize(),
            'grouped_match_users': grouped_results,
            'street_results': sorted(match_by_street_shoe_size(target_item), key=lambda k: k['occurences'], reverse=True),
            'match_results': sorted(results, key=lambda k: k['percentage'], reverse=True),
        })

# /apiv2/items/

@app.route('/apiv2/items/all/', methods=['GET'])
@app.cache.cached(timeout=14400)
def get_items_all():
    items = Item.query.all()
    results = []

    for item in items:
        results.append(item.minimal_serialize())

    return jsonify({
        'status': 'success',
        'message': '',
        'items': results
    })

@app.route('/apiv2/items/search/', methods=['POST'])
def post_items_search():
    queries = []

    if "search" in request.json:
        queries.append( or_(Brand.name.ilike('%' + request.json["search"].lower() + '%'), Item.model.ilike('%' + request.json["search"] + '%')) )

    items = Item.query.\
        join(Brand).\
        filter(*queries).\
        all()
        
    results = []

    for item in items:
        results.append(item.minimal_serialize())

    return jsonify({
        'status': 'success',
        'message': '',
        'items': results
    })


@app.route('/apiv2/items/sales/', methods=['POST'])
def get_items_sales():
    items_per_page = 30
    page = 1

    sort_order ='desc'
    sort = 'popularity'

    if request.json["page"]:
        page = request.json["page"]

    if "sort" in request.json:
        sort = request.json["sort"]

    if "sortOrder" in request.json:
        sort_order = request.json["sortOrder"]

    with open(current_app.config['ROOT_URL'] + 'outfile', 'rb') as fp:
        items = pickle.load(fp)

    if request.json["shoe_type"]:
        items = list(item for item in items if item["type"] in  request.json["shoe_type"])

    if "search" in request.json:
        def filterSearch(item):
            if(request.json["search"].lower() in item['brand']['name'] or request.json["search"].lower() in item['model']):
                return True
            else:
                return False
        items = list(filter(filterSearch, items))

    if "percent_off" in request.json:
        def filterPercentOff(item):
            for datafeed in item["datafeeds"]:
                if datafeed["Percent_Off"] >= int(request.json["percent_off"]):
                    return True
            return False
        items = list(filter(filterPercentOff, items))

    if "min_rating" in request.json:
        items = list(item for item in items if item["stats"]["avg_rating"] >= request.json["min_rating"])

    if "max_rating" in request.json:
        items = list(item for item in items if item["stats"]["avg_rating"] <= request.json["max_rating"])

    if "min_price" in request.json:
        def filterMinPrice(item):
            for datafeed in item["datafeeds"]:
                if float(datafeed["Product"]["Sale_Price"]) >= float(request.json["min_price"]):
                    return True
            return False
        items = list(filter(filterMinPrice, items))

    if "max_price" in request.json:
        def filterMaxPrice(item):
            for datafeed in item["datafeeds"]:
                if float(datafeed["Product"]["Sale_Price"]) <= float(request.json["max_price"]):
                    return True
            return False
        items = list(filter(filterMaxPrice, items))

    if request.json["gender"]:
        items = list(item for item in items if item["gender_id"] in  request.json["gender"])

    if request.json["brand"]:
        items = list(item for item in items if item["brand"]["id"] in  request.json["brand"])

    if request.json["mostCommonFit"]:
        items = list(item for item in items if item["stats"]["popular_fit_descriptor"] in  request.json["mostCommonFit"])
    
    if request.json["retailer"]:
        def filterRetailer(item):
            for datafeed in item["datafeeds"]:
                if datafeed["Retailer_Name"] in request.json["retailer"]:
                    return True
            return False
        items = list(filter(filterRetailer, items))

    def sortFunc(e):
        if (sort == 'retail_price'):
            return e['datafeeds'][0]['Product']['Retail_Price']
        if (sort == 'lowest_sale_price'):
            return e['lowest_sale_price']
        if (sort == 'popularity'):
            return e['stats']['count']
        if (sort == 'model'):
            return e['model']
        if (sort == 'brand_name'):
            return e['brand']['name']
        if (sort == 'popular_fit_descriptor'):
            return e['stats']['popular_fit_descriptor']
        if (sort == 'highest_rated_foot_shape'):
            return e['stats']['highest_rated_foot_shape']
        if (sort == 'avg_rating'):
            return e['stats']['avg_rating']
        return e['stats']['count']

    if (sort_order == 'desc'):
        items.sort(reverse=True, key=sortFunc)  
    if (sort_order == 'asc'):
        items.sort(key=sortFunc)  

    total = len(items)

    stop_num = page*items_per_page
    start_num = stop_num - 30

    items = items[start_num:stop_num]
    # items = [e.serialize() for e in items]

    return jsonify({
        'status': 'success',
        'message': '',
        'items': items,
        'count': total,
        'items_per_page': items_per_page
    })



@app.route('/apiv2/items/browse/', methods=['POST'])
@token_auth.login_required
def get_items_browse():
    items_per_page = 30
    page = 1

    sort_order ='desc'
    sort = 'popularity'

    if request.json["page"]:
        page = request.json["page"]

    if "sort" in request.json:
        sort = request.json["sort"]

    if "sortOrder" in request.json:
        sort_order = request.json["sortOrder"]

    queries = []
    
    if request.json["shoe_type"]:
        queries.append(Item.type.in_(request.json["shoe_type"]))

    if request.json["gender"]:
        queries.append(Item.gender_id.in_(request.json["gender"]))
    
    if request.json["brand"]:
        queries.append(Item.brand_id.in_(request.json["brand"]))

    if "min_rating" in request.json:
        queries.append(cast(Item.average_rating, Float()) >= request.json["min_rating"])

    if "max_rating" in request.json:
        queries.append(cast(Item.average_rating, Float()) <= request.json["max_rating"])

    if "search" in request.json:
        queries.append( or_(Brand.name.ilike('%' + request.json["search"].lower() + '%'), Item.model.ilike('%' + request.json["search"] + '%')) )

    if "rating_by_foot_shape_shape" in request.json:
        if request.json["rating_by_foot_shape_shape"] == 1:
            if "rating_by_foot_shape_max_rating" in request.json:
                queries.append( cast(Item.average_rating_egyptian, Float()) <= request.json["rating_by_foot_shape_max_rating"])
            if "rating_by_foot_shape_min_rating" in request.json:
                queries.append( cast(Item.average_rating_egyptian, Float()) >= request.json["rating_by_foot_shape_min_rating"])
        if request.json["rating_by_foot_shape_shape"] == 2:
            if "rating_by_foot_shape_max_rating" in request.json:
                queries.append( cast(Item.average_rating_roman, Float()) <= request.json["rating_by_foot_shape_max_rating"])
            if "rating_by_foot_shape_min_rating" in request.json:
                queries.append( cast(Item.average_rating_roman, Float()) >= request.json["rating_by_foot_shape_min_rating"])
        if request.json["rating_by_foot_shape_shape"] == 3:
            if "rating_by_foot_shape_max_rating" in request.json:
                queries.append( cast(Item.average_rating_greek, Float()) <= request.json["rating_by_foot_shape_max_rating"])
            if "rating_by_foot_shape_min_rating" in request.json:
                queries.append( cast(Item.average_rating_greek, Float()) >= request.json["rating_by_foot_shape_min_rating"])
        if request.json["rating_by_foot_shape_shape"] == 4:
            if "rating_by_foot_shape_max_rating" in request.json:
                queries.append( cast(Item.average_rating_germanic, Float()) <= request.json["rating_by_foot_shape_max_rating"])
            if "rating_by_foot_shape_min_rating" in request.json:
                queries.append( cast(Item.average_rating_germanic, Float()) >= request.json["rating_by_foot_shape_min_rating"])
        if request.json["rating_by_foot_shape_shape"] == 5:
            if "rating_by_foot_shape_max_rating" in request.json:
                queries.append( cast(Item.average_rating_celtic, Float()) <= request.json["rating_by_foot_shape_max_rating"])
            if "rating_by_foot_shape_min_rating" in request.json:
                queries.append( cast(Item.average_rating_celtic, Float()) >= request.json["rating_by_foot_shape_min_rating"])                                                

    if request.json["mostCommonFit"]:
        queries.append(Item.popular_fit_descriptor.in_(request.json["mostCommonFit"]))
        
    if "recommendedFootShape" in request.json:
        if request.json["recommendedFootShape"]:
            queries.append(Item.highest_rated_foot_shape.in_(request.json["recommendedFootShape"]))

    items = Item.query.\
        join(Brand).\
        filter(*queries).\
        all()

    def sortFunc(e):
        if (sort == 'popularity'):
            return len(e.user_items)
        if (sort == 'model'):
            return e.model
        if (sort == 'brand_name'):
            return e.brand.name
        if (sort == 'popular_fit_descriptor'):
            return e.popular_fit_descriptor
        if (sort == 'highest_rated_foot_shape'):
            return e.highest_rated_foot_shape  
        if (sort == 'avg_rating'):
            return e.average_rating
        return len(e.user_items)

    if (sort_order == 'desc'):
        items.sort(reverse=True, key=sortFunc)  
    if (sort_order == 'asc'):
        items.sort(key=sortFunc)  

    total = len(items)

    stop_num = page*items_per_page
    start_num = stop_num - 30

    items = items[start_num:stop_num]
    items = [e.serialize() for e in items]

    return jsonify({
        'status': 'success',
        'message': '',
        'items': items,
        'count': total,
        'items_per_page': items_per_page
    })

@app.route('/apiv2/recommend/', methods=['POST'])
@app.cache.cached(timeout=14400)
def recommend():
    queries = []

    # Only rocks shoes for now
    queries.append(Item.type == "rock")

    if request.json["gender"]:
        if request.json["gender"]["id"] != 0:
            genderNumber = int(request.json["gender"]["id"])
            queries.append(Item.gender_id.in_([3, genderNumber]))

    # only return items with more than 5 counts
    items = Item.query.\
        join(Brand).\
        outerjoin(Item.user_items).\
        group_by(Item).\
        filter(*queries).\
        having(func.count(Item.user_items) > 5).\
        all()

    def sortFootShape(e):
        if request.json["footShape"]["id"] == '1':
            return e.average_rating_egyptian
        if request.json["footShape"]["id"] == '2':
            return e.average_rating_roman
        if request.json["footShape"]["id"] == '3':
            return e.average_rating_greek
        if request.json["footShape"]["id"] == '4':
            return e.average_rating_germanic
        if request.json["footShape"]["id"] == '5': 
            return e.average_rating_celtic

    def sortCount(e):
        return len(e.user_items)

    def sortAvgRating(e):
        return e.average_rating

    # sort keys in ascending order of importance

    # count
    items.sort(reverse=True, key=sortCount)
    # avg rating
    items.sort(reverse=True, key=sortAvgRating)
    # foot shape
    if request.json["footShape"]:
        # 0 is prefer not to say
        if request.json["footShape"]["id"] != '0':
            # remove items without at least 5 reviews of foot shape
            # celtic/germanic have very low adoption, we move it down to 0
            if request.json["footShape"]["id"] == '1':
                items = [item for item in items if item.count_egyptian > 5]
            if request.json["footShape"]["id"] == '2':
                items = [item for item in items if item.count_roman > 5]
            if request.json["footShape"]["id"] == '3':
                items = [item for item in items if item.count_greek > 5]
            if request.json["footShape"]["id"] == '4':
                items = [item for item in items if item.count_germanic > 0]
            if request.json["footShape"]["id"] == '5': 
                items = [item for item in items if item.count_celtic > 0]

            items.sort(reverse=True, key=sortFootShape)

    itemsSliced = items[0:2]
    itemsSerialized = [e.serialize() for e in itemsSliced]

    for item in itemsSerialized:
        query = User_Item.query.filter(and_(
            User_Item.rating > 3, User_Item.comments != '', User_Item.item_id == item['id'])).order_by(User_Item.rating.desc()).limit(2).all()
        item["best_comments"] = []
        for bestComment in query:
            item["best_comments"].append({'user_id': bestComment.user_id,
                'size': bestComment.size,
                'size_standard': bestComment.size_standard,
                'target_item_size_in': bestComment.size_in,
                'target_item_id': bestComment.item_id,
                'comments': bestComment.comments,
                'rating': bestComment.rating,
                'fit_descriptor': bestComment.fit_descriptor,
                'user': bestComment.user.serialize_public()
            })
    return jsonify({
        'status': 'success',
        'message': '',
        'items': itemsSerialized,
    })

@app.route('/apiv2/items/brand/<brand_id>/', methods=['GET'])
@app.cache.cached(timeout=14400)
def get_items_brand(brand_id):

    brand_name = Brand.query.filter_by(id=brand_id).first()
    if not brand_name:
        abort(404)
    shoes = Item.query.filter_by(brand_id=brand_name.id).all()

    if not shoes:
        abort(404)
    else:
        return jsonify({
            'status': 'success',
            'message': '',
            'items': [e.serialize() for e in shoes]
        })


@app.route('/apiv2/items/popular/', methods=['GET'])
@app.cache.cached(timeout=14400)
def get_items_popular():
    all_user_items = User_Item.query.all()

    if not all_user_items:
        abort(404)
    else:
        user_items_array = []
        user_items_popular = []
        for user_item in all_user_items:
            user_items_array.append(
                {'user_id': user_item.user_id, 'item_id': user_item.item_id})

        user_item_count = Counter(d['item_id']
                                  for d in user_items_array).most_common(4)
        for item in user_item_count:
            mergedObject = Item.query.filter_by(id=item[0]).first().serialize()
            user_items_popular.append(mergedObject)

        return jsonify({
            'status': 'success',
            'message': '',
            'items': user_items_popular
        })

# /apiv2/item/


@app.route('/apiv2/item/details/<shoe_id>/', methods=['GET'])
def get_shoe_details(shoe_id):
    shoe = Item.query.filter_by(id=shoe_id).first()

    match_users = User_Item.query.filter(and_(func.length(User_Item.comments) > 3, User_Item.comments != '', User_Item.item_id == shoe_id)).all()
    match_users_with_comments = []
    for match_user in match_users:
        match_users_with_comments.append({
            'id': match_user.id,
            'user_id': match_user.user_id,
            'size': match_user.size,
            'size_standard': match_user.size_standard,
            'target_item_size_in': match_user.size_in,
            'target_item_id': match_user.item_id,
            'comments': match_user.comments,
            'comments_date_readable': match_user.comments_date_readable,
            'rating': match_user.rating,
            'fit_descriptor': match_user.fit_descriptor,
            'user': match_user.user.serialize_public()
        })

    # get sales for that shoe
    with open (current_app.config['ROOT_URL'] + 'outfile', 'rb') as fp:
        shoe_sale_links = pickle.load(fp)

    shoe_sale_match_0 = [x for x in shoe_sale_links if x['id'] == shoe.id]
    shoe_sale_links= []
    if shoe_sale_match_0:
        shoe_sale_links = [shoe_sale_match_0[0]]

    if not shoe:
        abort(404)
    else:
        return jsonify({
            'status': 'success',
            'message': '',
            'shoe_comments': match_users_with_comments,
            'shoe_sale_links': shoe_sale_links,
            'shoe': shoe.serialize()
        })


@app.route('/apiv2/item/edit/', methods=['POST'])
@token_auth.login_required
def edit_user_item():
    user_id = g.current_user.id
    user_item_id = request.json.get('userItemId')
    rating = request.json.get('rating')
    size = request.json.get('size')
    comments = request.json.get('comments')
    fit = request.json.get('fit')

    user_item = User_Item.query.filter_by(id=int(user_item_id)).first()
    if user_item and user_item.user_id == user_id:
        user_item.rating = rating
        user_item.comments = comments
        user_item.comments_date = datetime.datetime.now()
        user_item.size_in = convert_shoe_size_to_inches(size)
        user_item.size = size
        user_item.fit = fit
        db.session.commit()
        shoe_stats(user_item.item_id)
    else:
        abort(400)

    return jsonify({'status': "success", 'message': 'Shoe Edited', 'user_item': user_item.serialize()})


@app.route('/apiv2/item/add/', methods=['POST'])
@token_auth.login_required
def new_user_item():
    user_id = g.current_user.id
    item_id = request.json.get('itemId')
    rating = request.json.get('rating')
    comments = request.json.get('comments')
    fit = request.json.get('fit')
    size = request.json.get('size')

    if item_id and user_id:
        new_user_item = User_Item(user_id=user_id, item_id=item_id, rating=rating, size=size,
                                  size_in=convert_shoe_size_to_inches(size), comments=comments, 
                                  comments_date=datetime.datetime.now(), fit=fit)
        db.session.add(new_user_item)
        db.session.commit()
        shoe_stats(item_id)
    else:
        abort(500)

    return jsonify({'status': "success", 'message': 'Shoe Added', 'user_item': new_user_item.serialize()})


@app.route('/apiv2/item/remove/', methods=['POST'])
@token_auth.login_required
def delete_user_item():
    user_item_id = request.json.get('user_item_id')
    item_to_remove = User_Item.query.filter_by(id=int(user_item_id)).first()
    if item_to_remove:
        db.session.delete(item_to_remove)
        db.session.commit()
        shoe_stats(item_to_remove.item_id)
    else:
        abort(404)

    return jsonify({'status': "success", 'message': 'Shoe Deleted'})

@app.route('/apiv2/', defaults={'path': ''})
@app.route('/apiv2/<path:path>')
def catch_all_apiv2(path):
    if app.debug is not True:
        capture_message('404 - ' + request.path)
    return jsonify({'error': True, 'msg': 'API endpoint {!r} does not exist on this server'.format(request.path)}), 404
