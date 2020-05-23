import datetime
import re
from sqlalchemy import and_
from sizeSquirrel import app, db
from sizeSquirrel.models import *

from collections import Counter, defaultdict
import random

from sizeSquirrel.utils import list_all_brands, nearly_equal


def get_shoe_buddies(current_user_id, target_item_ids=None):
    target_users = []
    shoe_buddies = []

    if current_user_id is None:
        return shoe_buddies

    # get list of all of users items.
    user_items = User_Item.query.filter_by(user_id=current_user_id).all()
    if user_items:
        user_item_ids = []
        for sshoe in user_items:
            user_item_ids.append(sshoe.item_id)
        # if on private match add the target item to shoe buddy search
        if target_item_ids:
            user_who_have_target = User_Item.query.filter(User_Item.item_id.in_(
                target_item_ids)).filter(~User_Item.user_id.in_([current_user_id])).all()
            for user_item_target in user_who_have_target:
                target_users.append(
                    {'user_id': user_item_target.user_id, 'has_item_id': user_item_target.item_id})

        target_users_items = User_Item.query.filter(User_Item.item_id.in_(
            user_item_ids)).filter(~User_Item.user_id.in_([current_user_id]))

        for useritem in target_users_items:
            target_users.append(
                {'user_id': useritem.user_id, 'has_item_id': useritem.item_id})

        if target_users and len(target_users) > 0:
            # gets shoe match buddy
            shoe_buddies_count = sorted(Counter(d['user_id'] for d in target_users).most_common(
                10), key=lambda x: (-x[1], random.random()))
            if shoe_buddies_count:
                for buddy in shoe_buddies_count:
                    if target_item_ids:
                        # is it a match with target item:
                        match = User_Item.query.filter(and_(
                            User_Item.user_id == buddy[0], User_Item.item_id.in_(target_item_ids))).first()
                    else:
                        match = User_Item.query.filter(
                            User_Item.user_id == buddy[0]).first()
                    if len(shoe_buddies) < 3:
                        if target_item_ids:
                            if match:
                                shoe_buddies.append({
                                    'count_shoes': buddy[1],
                                    'username': User.query.filter_by(id=buddy[0]).first().serialize_public()['username'],
                                    'match': 'true' if match is not None else 'false'
                                })
                        else:
                            shoe_buddies.append({
                                'count_shoes': buddy[1],
                                'username': User.query.filter_by(id=buddy[0]).first().serialize_public()['username'],
                                'match': 'true' if match is not None else 'false'
                            })
    return shoe_buddies


def get_best_shoe_buddies(current_user_id):
    target_users = []
    best_shoe_buddies = []

    # get list of all of searchers shoes.
    my_items = User_Item.query.filter_by(user_id=current_user_id).all()
    for sshoe in my_items:
        # get list of users who have the same shoes searcher has in all sizes
        target_users_items = User_Item.query \
            .filter_by(item_id=sshoe.item_id) \
            .filter(~User_Item.user_id.in_([current_user_id]))

        # make a list of the users who have them in a nearly_equal size
        for useritem in target_users_items:
            if nearly_equal(float(sshoe.size_in), float(useritem.size_in)):
                target_users.append({
                    'user_id': useritem.user_id,
                    'has_item_id': useritem.item_id,
                    'has_item_size': useritem.size,
                    'has_item_size_in': useritem.size_in,
                    'user_username': useritem.user.username})

    if target_users and len(target_users) > 0:
        # gets shoe match buddies
        best_shoe_buddies_count = sorted(Counter(d['user_id'] for d in target_users).most_common(
            10), key=lambda x: (-x[1], random.random()))
        if best_shoe_buddies_count:
            for buddy in best_shoe_buddies_count:
                if buddy[1] > 0 and len(best_shoe_buddies) < 3:
                    best_shoe_buddies.append({
                        'count_shoes': buddy[1],
                        'username': User.query.filter_by(id=buddy[0]).first().serialize_public()['username']
                    })

    return best_shoe_buddies


def get_recommendations_by_shape(current_user_id, current_user_shape):
    if current_user_shape == 0:
        return []
    else:
        # get all users with same shoe shape
        all_users_with_shape = User.query \
            .filter_by(foot_shape=current_user_shape) \
            .filter(~User.id.in_([current_user_id]))

        current_users_items_array = []
        current_users_items = User_Item.query \
            .filter(User_Item.user_id.in_([current_user_id]))
        for user_item in current_users_items:
            current_users_items_array.append(user_item.item_id)

        # make array of users with same shoe shape
        target_users = []
        for user in all_users_with_shape:
            target_users.append(user.id)

        # get items rated highly by users with same shoe shape
        target_users_items = User_Item.query \
            .filter(User_Item.rating > int(4)) \
            .filter(~User_Item.item_id.in_(current_users_items_array)) \
            .filter(User_Item.user_id.in_(target_users))

        user_items_recommendations = []
        for user_item in target_users_items:
            user_items_recommendations.append({
                'id': user_item.id,
                'rating': user_item.rating,
                'item_id': user_item.item_id
            })

        target_recommendations = []
        user_item_count = Counter(d['item_id']
                                  for d in user_items_recommendations).most_common(3)
        for item in user_item_count:
            if item[1] >= 5:
                target_recommendations.append({
                    'count': item[1],
                    'item': Item.query.filter_by(id=item[0]).first().serialize(),
                })

        return target_recommendations
