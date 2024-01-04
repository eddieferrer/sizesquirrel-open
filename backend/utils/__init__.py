import re
from backend import app, db
from backend.emails import send_email
from collections import Counter, defaultdict
from sqlalchemy import func

from backend.models import *

# debugging function to pretty print dict

def pretty_print_dict(d, indent=0):
    for key, value in iter(d.items()):
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty_print_dict(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


def find_in_brands(brand_name):
    brands = Brand.query.all()
    for brand in brands:
        if brand.name == brand_name.lower():
            return True
    return False


def list_all_brands():
    brands = Brand.query.all()
    arrayOfBrands = [e.serialize() for e in brands]
    arrayOfBrands.sort(key=lambda x: x['name'], reverse=False)
    return arrayOfBrands


def list_all_items():
    items = Item.query.all()
    return [e.serialize() for e in items]


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


def convert_shoe_size_to_inches(size):
    if size is None:
        return ""
    size = float(size)
    # takes an agnostic shoe size, stores it as inches
    size_in_inches = 0

    if size > 32:
        # we're inputing a EUR size
        size_in_inches = ((size - 31.333) / 1.333 + 1)/3 + 7.333
    else:
        # we're inputing a US size
        size_in_inches = (size * .333) + 7.333
    return float("{0:.2f}".format(size_in_inches))


def nearly_equal(shoe1, shoe2):
    if convert_shoe_size_to_standards(shoe1)['EUR'] == convert_shoe_size_to_standards(shoe2)['EUR']:
        return True
    if convert_shoe_size_to_standards(shoe1)['USM'] == convert_shoe_size_to_standards(shoe2)['USM']:
        return True
    else:
        return False

def clean_string_for_match(string):
    string = string.replace(' GTX', '')
    string = string.replace(' gtx', '')
    string = string.replace(' Gore-Tex(R)', '')
    string = string.replace(' Gore-Tex', '')
    string = string.replace(' GV', '')
    string = string.replace(' gv', '')
    string = string.replace(' RR', '')
    string = string.replace('(For Men and Women)', '')
    return string

# takes a long string (usually affiliate product title), and model and brand and sees if they are the same


def match_strings(product_title, brand_name, item):
    model = item["model"]
    brand = item["brand"]["name"]
    gender = item["gender_id"]

    # lets remove certain annoying words from model
    model = clean_string_for_match(model)

    # Special case for harnesses with same models as shoes
    # if product title contains 'harness' in lower or upper case return false
    if 'harness' in product_title.lower():
        return False

    # lets remove annoying words from product title
    product_title = clean_string_for_match(product_title)

    model_ss = item["model"].replace('-', ' ')
    model_ss = model_ss.replace('ii', 'II')
    model_ss = model_ss.lower()
    model_with_dash = item["model"]

    # lets remove ' for arcteryx
    brand_name = brand_name.replace('\'', '')
    # replace brand names in feeds
    brand_name = brand_name.replace('Climb-X', 'Climb X')
    brand_name = brand_name.replace('Five.Ten', 'Five Ten')
    brand_name = brand_name.replace('Black Diamond Equipment', 'Black Diamond')
    brand_name = brand_name.replace('So Ill Holds', 'So Ill')

    brand_name_result = re.findall(
        '\\b'+brand+'\\b', brand_name, flags=re.IGNORECASE)
    brand_result = re.findall(
        '\\b'+brand+'\\b', product_title, flags=re.IGNORECASE)

    model_result = re.findall(
        '\\b'+model+'\\b', product_title, flags=re.IGNORECASE)
    women_result = re.findall(
        '\\b'+'women'+'\\b', product_title, flags=re.IGNORECASE)

    if len(brand_result) > 0 or len(brand_name_result) > 0:
        if len(model_result) > 0:

            shoe = Item.query.filter(Item.brand_id == item["brand"]["id"]).filter(
                func.lower(Item.model).like('%'+model+'%')).all()
            if not shoe:
                shoe = Item.query.filter(Item.brand_id == item["brand"]["id"]).filter(
                    func.lower(Item.model).like('%'+model_with_dash+'%')).all()

            for shoe_single in shoe:
                if len(shoe) != 1:
                    if shoe_single.model != item["model"]:
                        shoe_array = {
                            'model': shoe_single.model,
                            'gender_id': shoe_single.gender_id,
                            'brand': {
                                'name': shoe_single.brand.name,
                                'id': shoe_single.brand.id
                            }
                        }
                        if match_strings(product_title, brand_name, shoe_array) is True:
                            return False
                    else:
                        # shoe is available in 2 genders or more
                        if len(women_result) == 0:
                            women_result = re.findall(
                                '\\b'+'womens'+'\\b', product_title, flags=re.IGNORECASE)
                        if len(women_result) == 0:
                            women_result = re.findall(
                                '\\b'+'wmns'+'\\b', product_title, flags=re.IGNORECASE)
                        if len(women_result) == 0:
                            women_result = re.findall(
                                '\\b'+'women\'s'+'\\b', product_title, flags=re.IGNORECASE)

                        if len(model_result) > 0:
                            if len(women_result) > 0 and gender == 2:
                                # it's a womens shoe
                                return True

                            if len(women_result) == 0:
                                if gender == 1 or gender == 3:
                                    return True

                            return False
                        else:
                            return False
                else:
                    # shoe only available in 1 gender
                    # len(shoe == 1)
                    return True
        else:
            # len(model_result) == 0:
            return False
    else:
        # len(brand_result) == 0 or len(brand_name_result) == 0:
        return False

