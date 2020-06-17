from datetime import datetime, timedelta
from sqlalchemy import and_

from backend import app, db
from backend.models import User_Item, User, Item, convert_shoe_size_to_standards
from collections import Counter
from flask import Flask, g
from backend.utils import pretty_print_dict, nearly_equal

# main matching algorithm. Takes have_item_id, have_item_size, want_item_id


def match_function(have_item_id, have_item_size_in, want_item_id):
    users_with_have_item = []

    dict_of_users = {}
    # make a list of users who have 'have item'.
    if 'current_user' in g and g.current_user is not None:
        target_users__have = User_Item.query.filter(and_(
            User_Item.user_id != g.current_user.id, User_Item.item_id == have_item_id)).all()
    else:
        target_users__have = User_Item.query.filter(
            User_Item.item_id == have_item_id).all()

    if target_users__have:
        for useritem in target_users__have:
            users_with_have_item.append(useritem.user_id)
            dict_of_users[useritem.user_id] = {
                have_item_id: {
                    'has_item_id': useritem.item_id,
                    'has_item_size': useritem.size,
                    'has_item_size_in': useritem.size_in
                }
            }

        # make a list of users who have 'want item'.
        target_users__want = User_Item.query.filter(User_Item.user_id.in_(
            users_with_have_item)).filter_by(item_id=want_item_id)

        if target_users__want:
            for useritem in target_users__want:
                # user has 'have item'
                if useritem.user_id in dict_of_users:
                    dict_of_users[useritem.user_id][have_item_id]['want_item_id'] = useritem.item_id
                    dict_of_users[useritem.user_id][have_item_id]['want_item_size'] = useritem.size
                    dict_of_users[useritem.user_id][have_item_id]['want_item_size_in'] = useritem.size_in

                    dict_of_users[useritem.user_id][have_item_id]['user_id'] = useritem.user_id
                    dict_of_users[useritem.user_id][have_item_id]['want_item_size_standard'] = useritem.size_standard
                    dict_of_users[useritem.user_id][have_item_id]['want_item_comments'] = useritem.comments
                    dict_of_users[useritem.user_id][have_item_id]['want_item_rating'] = useritem.rating
                    dict_of_users[useritem.user_id][have_item_id]['want_item_fit_descriptor'] = useritem.fit_descriptor

            for key in list(dict_of_users):
                # iterate through dict, remove users who dont have both want and have
                # add size delta to users who have both items
                if all(k in dict_of_users[key][have_item_id] for k in ("want_item_id", "has_item_id")):

                    user = User.query.filter_by(id=key).first()

                    size_delta = float(dict_of_users[key][have_item_id]['want_item_size_in']) - float(
                        dict_of_users[key][have_item_id]['has_item_size_in'])
                    dict_of_users[key][have_item_id]['size_delta'] = size_delta
                    dict_of_users[key][have_item_id]['recommended_size_in'] = have_item_size_in + size_delta
                    dict_of_users[key][have_item_id]['recommended_size'] = convert_shoe_size_to_standards(
                        have_item_size_in + size_delta)
                    dict_of_users[key][have_item_id]['username'] = user.username
                else:
                    del dict_of_users[key]

            # print pretty_print_dict(dict_of_users)

            return dict_of_users
        else:
            # return empty dict if no matches for want item
            return {}

# process results dict


def process_results_dict(results_dict):
    # print pretty_print_dict(results_dict)
    results = []
    if results_dict:
        for user in results_dict:
            for user_shoe_dict in results_dict[user]:
                # print results_dict[user]
                list_match = [x for x in results if nearly_equal(float(x['size_in'][0]), float(
                    results_dict[user][user_shoe_dict]['recommended_size_in']))]
                if not list_match:
                    results_length = sum(len(v)
                                         for v in iter(results_dict.values())) 
                    results.append({
                        'size_in': [results_dict[user][user_shoe_dict]['recommended_size_in']],
                        'occurences': 1,
                        'total_matches': results_length,
                        'percentage': round(100 * float(1)/float(results_length), 2),
                    })
                else:
                    list_match[0]['size_in'].append(
                        results_dict[user][user_shoe_dict]['recommended_size_in'])
                    list_match[0]['occurences'] += 1
                    list_match[0]['percentage'] = round(
                        100 * float(list_match[0]['occurences'])/float(list_match[0]['total_matches']), 2)

                for result in results:
                    result['size_standard'] = convert_shoe_size_to_standards(
                        Counter(d for d in result['size_in']).most_common(1)[0][0])

    return results


def match_by_street_shoe_size(target_item):
    target_users = []
    street_results = []

    if not g.current_user.street_shoe_size_in:
        return street_results

    # lets get a list of users who have target item, exclude searcher
    match = User_Item.query.filter_by(item_id=target_item.id).filter(
        ~User_Item.user_id.in_([g.current_user.id]))
    for match_information in match:
        matched_user = User.query.filter_by(
            id=match_information.user_id).first()
        # user has a street size
        if matched_user.street_shoe_size_in:
            # user matches in one of the standards
            # we only need eur and usm, other standards are generated from those
            if nearly_equal(float(g.current_user.street_shoe_size_in), float(matched_user.street_shoe_size_in)):
                target_users.append({
                    'size_in': match_information.size_in,
                    'user_id': match_information.user_id,
                    'has_item_id': match_information.item_id,
                    'has_item_size': match_information.size})

    for user in target_users:
        list_match = [x for x in street_results if nearly_equal(
            float(x['size_in'][0]), float(user['size_in']))]
        if not list_match:
            street_results.append({
                'size_in': [user['size_in']],
                'occurences': 1,
                'total_matches': len(target_users),
                'percentage': round(100 * float(1)/float(len(target_users)), 2),
            })
        else:
            list_match[0]['size_in'].append(user['size_in'])
            list_match[0]['occurences'] += 1
            list_match[0]['percentage'] = round(
                100 * float(list_match[0]['occurences'])/float(list_match[0]['total_matches']), 2)

        for result in street_results:
            result['size_standard'] = convert_shoe_size_to_standards(
                Counter(d for d in result['size_in']).most_common(1)[0][0])

    return street_results
