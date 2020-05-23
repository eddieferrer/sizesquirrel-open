from sizeSquirrel import app, db
from sizeSquirrel.models import Item, User_Item, User

from collections import Counter

def set_stats_items():
    items = Item.query.all()
    for item in items:
        shoe_stats(item.id)

def set_stats_specific_item(shoe_id):
    item = Item.query.filter_by(id=shoe_id).first()
    shoe_stats(item.id)

def shoe_stats(shoe_id):
    item = Item.query.filter_by(id=shoe_id).first()

    item.average_rating = average_rating(item)
    
    shoe_stats = shoe_stats_rating_by_footshape(shoe_id)

    item.average_rating_egyptian = shoe_stats[0]["avg_rating"]
    item.count_egyptian = shoe_stats[0]["count"]

    item.average_rating_roman = shoe_stats[1]["avg_rating"]
    item.count_roman = shoe_stats[1]["count"]

    item.average_rating_greek = shoe_stats[2]["avg_rating"]
    item.count_greek = shoe_stats[2]["count"]

    item.average_rating_germanic = shoe_stats[3]["avg_rating"]
    item.count_germanic = shoe_stats[3]["count"]

    item.average_rating_celtic = shoe_stats[4]["avg_rating"]
    item.count_celtic = shoe_stats[3]["count"]

    itemCount = len(item.user_items)
    item.popular_foot_shape = popular_foot_shape(shoe_stats,itemCount)

    item.highest_rated_foot_shape = highest_rated_foot_shape(shoe_stats)

    item.popular_fit_descriptor = popular_fit_descriptor(item)

    by_skill_stats = shoe_stats_rating_by_climb_skill(shoe_id)
    item.average_rating_beginner_climbers = by_skill_stats[0]["avg_rating"]
    item.count_beginner_climbers = by_skill_stats[0]["count"]
    item.average_rating_advanced_climbers = by_skill_stats[1]["avg_rating"]
    item.count_advanced_climbers = by_skill_stats[1]["count"]
    item.average_rating_expert_climbers = by_skill_stats[2]["avg_rating"]
    item.count_expert_climbers = by_skill_stats[2]["count"]

    db.session.commit()

def highest_rated_foot_shape(shoe_stats):
    # remove ratings of less than or equal to 5 count, 
    # has to match UI in FindMySizeBlock
    filteredList = [item for item in shoe_stats if item["count"] > 5]
    # sort by highest average rating
    sortedList = sorted(filteredList, key=lambda x: x["avg_rating"], reverse=True)
    # return first item, only descriptor
    if len(sortedList) == 0:
        return "N/A"
    if len(sortedList) > 1:
        if sortedList[0]["avg_rating"] == sortedList[1]["avg_rating"]:
            return sortedList[0]["foot_shape_descriptor"] + ' or ' + sortedList[1]["foot_shape_descriptor"]
    return sortedList[0]["foot_shape_descriptor"]

def average_rating(item):
    if len(item.user_items) == 0:
        average_rating = 0
    else:
        sum_rating = 0
        for user_item in item.user_items:
            sum_rating += user_item.rating

        average_rating = float(sum_rating) / float(len(item.user_items))
    return round(average_rating, 4)

def shoe_stats_rating_by_footshape(shoe_id):
    # returns ratings/totals per foot shape
    user_items = db.session.query(User_Item, User).filter(
        User_Item.item_id == shoe_id).filter(User_Item.user_id == User.id).all()

    user_items_foot_shape1 = []
    user_items_foot_shape2 = []
    user_items_foot_shape3 = []
    user_items_foot_shape4 = []
    user_items_foot_shape5 = []

    sum_rating_foot_shape1 = 0
    sum_rating_foot_shape2 = 0
    sum_rating_foot_shape3 = 0
    sum_rating_foot_shape4 = 0
    sum_rating_foot_shape5 = 0

    for user_item in user_items:
        if user_item.User.foot_shape == 1:
            sum_rating_foot_shape1 += user_item.User_Item.rating
            user_items_foot_shape1.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })
        if user_item.User.foot_shape == 2:
            sum_rating_foot_shape2 += user_item.User_Item.rating
            user_items_foot_shape2.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })
        if user_item.User.foot_shape == 3:
            sum_rating_foot_shape3 += user_item.User_Item.rating
            user_items_foot_shape3.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })
        if user_item.User.foot_shape == 4:
            sum_rating_foot_shape4 += user_item.User_Item.rating
            user_items_foot_shape4.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })
        if user_item.User.foot_shape == 5:
            sum_rating_foot_shape5 += user_item.User_Item.rating
            user_items_foot_shape5.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })

    count_1 = len(user_items_foot_shape1)
    count_2 = len(user_items_foot_shape2)
    count_3 = len(user_items_foot_shape3)
    count_4 = len(user_items_foot_shape4)
    count_5 = len(user_items_foot_shape5)

    if count_1 > 0:
        avg_1 = float(sum_rating_foot_shape1) / float(count_1)
    else:
        avg_1 = 0

    if count_2 > 0:
        avg_2 = float(sum_rating_foot_shape2) / float(count_2)
    else:
        avg_2 = 0

    if count_3 > 0:
        avg_3 = float(sum_rating_foot_shape3) / float(count_3)
    else:
        avg_3 = 0

    if count_4 > 0:
        avg_4 = float(sum_rating_foot_shape4) / float(count_4)
    else:
        avg_4 = 0

    if count_5 > 0:
        avg_5 = float(sum_rating_foot_shape5) / float(count_5)
    else:
        avg_5 = 0

    ratings = [
        {
            'foot_shape_descriptor': 'Egyptian',
            'foot_shape_descriptor_id': 1,
            'avg_rating': float("{0:.2f}".format(avg_1)),
            'count': count_1
        },
        {
            'foot_shape_descriptor': 'Roman',
            'foot_shape_descriptor_id': 2,
            'avg_rating': float("{0:.2f}".format(avg_2)),
            'count': count_2
        },
        {
            'foot_shape_descriptor': 'Greek',
            'foot_shape_descriptor_id': 3,
            'avg_rating': float("{0:.2f}".format(avg_3)),
            'count': count_3
        },
        {
            'foot_shape_descriptor': 'Germanic',
            'foot_shape_descriptor_id': 4,
            'avg_rating': float("{0:.2f}".format(avg_4)),
            'count': count_4
        },
        {
            'foot_shape_descriptor': 'Celtic',
            'foot_shape_descriptor_id': 5,
            'avg_rating': float("{0:.2f}".format(avg_5)),
            'count': count_5
        }
    ]
    return ratings

def shoe_stats_rating_by_climb_skill(shoe_id):
    # returns ratings/totals per foot shape
    user_items = db.session.query(User_Item, User).filter(
        User_Item.item_id == shoe_id).filter(User_Item.user_id == User.id).all()

    # Bouldering
    # Beginner, 1 - 3
    # Advanced, 4 - 7
    # Expert, 8 - 14

    # Sport
    # Beginner, 1 - 9
    # Advanced, 10 - 18
    # Expert, 19 - 26

    # Trad
    # Beginner, 1 - 9
    # Advanced, 10 - 18
    # Expert, 19 - 26

    user_items_beginner = []
    user_items_advanced = []
    user_items_expert = []

    sum_rating_beginner = 0
    sum_rating_advanced = 0
    sum_rating_expert = 0

    for user_item in user_items:
        # beginner skill
        if 1 <= user_item.User.climbing_boulder <= 3 or \
            1 <= user_item.User.climbing_sport <= 9 or \
            1 <= user_item.User.climbing_trad <= 9:

            sum_rating_beginner += user_item.User_Item.rating
            user_items_beginner.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })
        # advanced skill
        if 4 <= user_item.User.climbing_boulder <= 7 or \
            10 <= user_item.User.climbing_sport <= 18 or \
            10 <= user_item.User.climbing_trad <= 18:

            sum_rating_advanced += user_item.User_Item.rating
            user_items_advanced.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })
        # expert skill
        if 8 <= user_item.User.climbing_boulder <= 14 or \
            19 <= user_item.User.climbing_sport <= 26 or \
            19 <= user_item.User.climbing_trad <= 26:

            sum_rating_expert += user_item.User_Item.rating
            user_items_expert.append({
                'user_item_rating': user_item.User_Item.rating,
                'user_id': user_item.User.id,
                'user_username': user_item.User.username,
                'user_foot_shape': user_item.User.foot_shape
            })

    count_1 = len(user_items_beginner)
    count_2 = len(user_items_advanced)
    count_3 = len(user_items_expert)

    if count_1 > 0:
        avg_1 = float(sum_rating_beginner) / float(count_1)
    else:
        avg_1 = 0

    if count_2 > 0:
        avg_2 = float(sum_rating_advanced) / float(count_2)
    else:
        avg_2 = 0

    if count_3 > 0:
        avg_3 = float(sum_rating_expert) / float(count_3)
    else:
        avg_3 = 0

    ratings = [
        {
            'skill': 'beginner',
            'avg_rating': float("{0:.2f}".format(avg_1)),
            'count': count_1
        },
        {
            'skill': 'advanced',
            'avg_rating': float("{0:.2f}".format(avg_2)),
            'count': count_2
        },
        {
            'skill': 'expert',
            'avg_rating': float("{0:.2f}".format(avg_3)),
            'count': count_3
        },
    ]
    return ratings

# Based on %
def popular_foot_shape(shoe_stats, totalCount):
    if totalCount == 0:
        return 'None'
    max_count = max([
        round(shoe_stats[0]["count"]/totalCount,2), 
        round(shoe_stats[1]["count"]/totalCount,2), 
        round(shoe_stats[2]["count"]/totalCount,2), 
        round(shoe_stats[3]["count"]/totalCount,2), 
        round(shoe_stats[4]["count"]/totalCount,2)
    ])
    most_popular = ''
    most_popular_obj = [x for x in shoe_stats if x["count"] == max_count]
    for idx, item in enumerate(most_popular_obj):
        if idx > 0:
            most_popular = most_popular + ' & ' + item['foot_shape_descriptor']
        else:
            most_popular = item['foot_shape_descriptor']
    return most_popular

def popular_fit_descriptor(item):
    if len(item.user_items) == 0:
        return "Normal"

    fit_descriptor_array = []
    for user_item in item.user_items:
        fit_descriptor_array.append(user_item.fit_descriptor)

    popular_fit_descriptor = Counter(
        d for d in fit_descriptor_array).most_common(1)

    if popular_fit_descriptor:
        fitString = popular_fit_descriptor[0][0]
    else:
        fitString = "Normal"
    return fitString