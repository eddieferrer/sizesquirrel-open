import re
import json
import pickle
from collections import Counter
from sqlalchemy import Float
from flask import Flask, jsonify, abort, request, g
from backend import app
from backend.models import User, User_Item, Item, Brand
from backend.utils import match_strings
from backend.avantlink.process_data_feeds import DATA_FEED_INFO_ARRAY, clean_up_feed

from .views import token_auth

# /apiv2/admin/

@app.route('/apiv2/admin/stats/', methods=['GET'])
@token_auth.login_required
def get_admin_stats():
    if g.current_user.email == "eferrer@gmail.com" and g.current_user.id == 1:
        all_user_items = User_Item.query.all()
        all_users = User.query.all()
        shoes = Item.query.all()
        users_with_split_shoes_1 = User.query.filter_by(
            split_shoe_info=1).count()
        users_with_split_shoes_2 = User.query.filter_by(
            split_shoe_info=2).count()

        users_with_gender_0 = User.query.filter_by(gender=0).count()
        users_with_gender_1 = User.query.filter_by(gender=1).count()
        users_with_gender_2 = User.query.filter_by(gender=2).count()

        # users_with_boulder = User.query.filter(User.climbing_boulder > 0).all()
        # users_with_sport = User.query.filter(User.climbing_sport > 0).all()
        # users_with_trad = User.query.filter(User.climbing_trad > 0).all()
        users_with_boulder =  User.query.filter(User.climbing_boulder > 0).count()
        users_with_sport = User.query.filter(User.climbing_sport > 0).count()
        users_with_trad = User.query.filter(User.climbing_trad > 0).count()

        user_item_count_array = []
        user_item_count_array_not_rock = []
        for user_item in all_user_items:
            if user_item.item.type != 'rock':
                user_item_count_array_not_rock.append(
                    {'user_id': user_item.user_id, 'item_id': user_item.item_id})
            user_item_count_array.append(
                {'user_id': user_item.user_id, 'item_id': user_item.item_id})

        user_items = []
        user_item_count = Counter(d['item_id']
                                  for d in user_item_count_array).most_common(10)
        for item in user_item_count:
            user_items.append({
                'count': item[1],
                'item': Item.query.filter_by(id=item[0]).first().serialize(),
            })

        user_items_not_rock = []
        user_item_count_not_rock = Counter(
            d['item_id'] for d in user_item_count_array_not_rock).most_common(10)
        for item in user_item_count_not_rock:
            user_items_not_rock.append({
                'count': item[1],
                'item': Item.query.filter_by(id=item[0]).first().serialize(),
            })

        users_with_items = []
        users_with_items_count = Counter(
            d['user_id'] for d in user_item_count_array).most_common()
        for user in users_with_items_count:
            users_with_items.append({
                'count': user[1],
                'user': User.query.filter_by(id=user[0]).first().serialize_private(),
            })
        average_count_per_user = float(
            sum(d['count'] for d in users_with_items))/len(users_with_items)
        users_with_the_most_items = users_with_items[:12]

        users_with_popular1 = []
        for item in user_item_count_array:
            if item['item_id'] == user_items[0]['item']['id']:
                users_with_popular1.append(item['user_id'])
        user_items_popular1 = []
        user_item_popular1 = Counter(
            d['item_id'] for d in user_item_count_array if d['user_id'] in users_with_popular1).most_common(4)
        for item in user_item_popular1:
            user_items_popular1.append({
                'count': item[1],
                'item': Item.query.filter_by(id=item[0]).first().serialize(),
            })
        users_with_popular2 = []
        for item in user_item_count_array:
            if item['item_id'] == user_items[1]['item']['id']:
                users_with_popular2.append(item['user_id'])
        user_items_popular2 = []
        user_item_popular2 = Counter(
            d['item_id'] for d in user_item_count_array if d['user_id'] in users_with_popular2).most_common(4)
        for item in user_item_popular2:
            user_items_popular2.append({
                'count': item[1],
                'item': Item.query.filter_by(id=item[0]).first().serialize(),
            })

        users_with_popular3 = []
        for item in user_item_count_array:
            if item['item_id'] == user_items[2]['item']['id']:
                users_with_popular3.append(item['user_id'])
        user_items_popular3 = []
        user_item_popular3 = Counter(
            d['item_id'] for d in user_item_count_array if d['user_id'] in users_with_popular3).most_common(4)
        for item in user_item_popular3:
            user_items_popular3.append({
                'count': item[1],
                'item': Item.query.filter_by(id=item[0]).first().serialize(),
            })

        users_with_footshape_1 = []
        for user in all_users:
            if user.foot_shape == 1:
                users_with_footshape_1.append({
                    'foot_shape': user.foot_shape,
                    'username': user.username})

        users_with_footshape_2 = []
        for user in all_users:
            if user.foot_shape == 2:
                users_with_footshape_2.append({
                    'foot_shape': user.foot_shape,
                    'username': user.username})

        users_with_footshape_3 = []
        for user in all_users:
            if user.foot_shape == 3:
                users_with_footshape_3.append({
                    'foot_shape': user.foot_shape,
                    'username': user.username})

        users_with_footshape_4 = []
        for user in all_users:
            if user.foot_shape == 4:
                users_with_footshape_4.append({
                    'foot_shape': user.foot_shape,
                    'username': user.username})

        users_with_footshape_5 = []
        for user in all_users:
            if user.foot_shape == 5:
                users_with_footshape_5.append({
                    'foot_shape': user.foot_shape,
                    'username': user.username})

        return jsonify({
            'status': 'success',
            'shoes_count': len(shoes),
            'average_count_per_user': format(average_count_per_user, '.2f'),
            'all_user_items_count': len(all_user_items),
            'all_users_count': len(all_users),
            'users_with_gender_0': users_with_gender_0,
            'users_with_gender_1': users_with_gender_1,
            'users_with_gender_2': users_with_gender_2,
            'users_with_split_shoes_1': users_with_split_shoes_1,
            'users_with_split_shoes_2': users_with_split_shoes_2,
            'users_with_footshape_1': users_with_footshape_1,
            'users_with_footshape_2': users_with_footshape_2,
            'users_with_footshape_3': users_with_footshape_3,
            'users_with_footshape_4': users_with_footshape_4,
            'users_with_footshape_5': users_with_footshape_5,
            'user_item_count': user_items,
            'user_item_count_not_rock': user_items_not_rock,
            'users_with_the_most_items': users_with_the_most_items,
            'user_items_popular1': user_items_popular1,
            'user_items_popular2': user_items_popular2,
            'user_items_popular3': user_items_popular3,
            'users_with_boulder': users_with_boulder,
            'users_with_trad': users_with_trad,
            'users_with_sport': users_with_sport,
        })

    else:
        return jsonify({
        'status': 'error',
        'message': 'You are not authorized to view this pages.'
    }), 401


@app.route('/apiv2/admin/matchtest/', methods=['POST'])
@token_auth.login_required
def get_admin_matchtest():
    if g.current_user.email == "eferrer@gmail.com" and g.current_user.id == 1:
        match_test_item_id = request.json.get('matchTestItemId')
        item = Item.query.filter_by(id=match_test_item_id).first().serialize()

        raw_data_feeds = DATA_FEED_INFO_ARRAY

        match_test = []
        for feed in raw_data_feeds:
            feed = clean_up_feed(feed)
            
            for product in feed["datafeed"]:
                match_test.append({
                    "DataFeed Product_Name": product["Product_Name"],
                    "DataFeed Brand_Name": product["Brand_Name"],
                    "Match": match_strings(product["Product_Name"], product["Brand_Name"], item),
                    'Retailer_Name': feed["retailer_name"]
                })

        return jsonify({
            'status': 'success',
            'matchTestItemId': match_test_item_id,
            'matchTest': match_test
        })

    else:
        return jsonify({
        'status': 'error',
        'message': 'You are not authorized to view this pages.'
    }), 401

