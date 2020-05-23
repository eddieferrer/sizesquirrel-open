from flask import Flask, request, current_app
import json
from datetime import datetime, timedelta
from amazon.api import AmazonAPI
from sizeSquirrel import app, db
from sizeSquirrel.models import Item

AMAZON_ACCESS_KEY = current_app.config['AMAZON_ACCESS_KEY']
AMAZON_SECRET_KEY = current_app.config['AMAZON_SECRET_KEY']
AMAZON_ASSOC_TAG = current_app.config['AMAZON_ASSOC_TAG']

# Amazon Nodes
# Clothing Shoes Jewelry Men Shoes Outdoor Climbing: 679270011
# Clothing Shoes Jewelry Men Shoes Boots: 679307011
# Clothing Shoes Jewelry Men Shoes Outdoor Hiking & Trekking Hiking Boots: 679280011
# Clothing Shoes Jewelry Women Shoes Outdoor Climbing: 679350011
# Clothing Shoes Jewelry Women Shoes Boots: 679380011
# Clothing Shoes Jewelry Women Shoes Outdoor Hiking & Trekking Hiking Shoes: 679357011

# def amazon_api_sales():
#     amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
#
#     sales_list = []
#
#     try:
#         products = amazon.search(Keywords='Rock Climbing Shoe', SearchIndex='SportingGoods', MinPercentageOff='20', Sort='sale-flag', ResponseGroup='VariationSummary, Large', Condition='All', Availability='Available', BrowseNode="679270011")
#
#         for product in products:
#             # print product.parsed_response.__dict__
#             if hasattr(product, 'parsed_response'):
#                 if hasattr(product.parsed_response, 'VariationSummary'):
#                     # print product.parsed_response.__dict__
#                     productinfo = {}
#                     productinfo["title"] = product.title
#                     productinfo["variation_summary"] = product.parsed_response.VariationSummary
#                     productinfo["small_image_url"] = product.small_image_url
#                     productinfo["medium_image_url"] = product.medium_image_url
#                     productinfo["asin"] = product.asin
#                     productinfo["offer_url"] = product.offer_url
#                     productinfo["item_attributes"] =  product.parsed_response.ItemAttributes
#                     sales_list.append(productinfo)
#     except:
#         pass
#     return sales_list

# Get Amazon API Info
# small image = 75x70
# medium image = 160x150
@app.route('/amazon_api/search/', methods = ['POST'])
def amazon_api_request():
    item_id = request.json.get('item_id')
    brand = request.json.get('brand')
    model = request.json.get('model')

    item = Item.query.filter_by(id=item_id).first()

    amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

    browse_modes = ["679270011","679350011","679307011","679380011","679380011","679280011","679357011"]

    if item:
        # loop through browseNodes
        for node in browse_modes:
            try:
                products = amazon.search_n(1, Brand=brand, Title=model, SearchIndex='SportingGoods', ResponseGroup='VariationSummary, Large', BrowseNode=node)

                product_info = {
                    'title': products[0].title,
                    'small_image_url': products[0].small_image_url,
                    'medium_image_url': products[0].medium_image_url,
                    'asin': products[0].asin,
                }

                item.small_image_url=products[0].small_image_url
                item.medium_image_url=products[0].medium_image_url
                item.offer_url=products[0].offer_url

                if item.asin and products[0].asin not in item.asin:
                    item.asin = item.asin + ',' + products[0].asin
                else:
                    item.asin = products[0].asin
                item.thumbnail_cache=datetime.utcnow()
                db.session.commit()

                return json.dumps(product_info)
            except:
                pass
        else:
            # error
            error = {
                'error': 'amazon api exception'
            }
            return json.dumps(error)



# Not currently used
@app.route('/amazon_api/price/', methods = ['POST'])
def amazon_api_request_price():
    item_id = request.json.get('item_id')
    brand = request.json.get('brand')
    model = request.json.get('model')

    item = Item.query.filter_by(id=item_id).first()

    amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

    if item:
        try:
            products = amazon.search_n(1, Brand=brand, Title=model, SearchIndex='SportingGoods', ResponseGroup='VariationSummary')
            product_info = {
                'offer_url': products[0].offer_url,
                'variation_summary': {
                    'LowestPrice': {
                        'FormattedPrice': products[0].parsed_response.VariationSummary.LowestPrice["FormattedPrice"].text,
                        'Amount': products[0].parsed_response.VariationSummary.LowestPrice["Amount"].text
                    },
                    'HighestPrice': {
                        'FormattedPrice': products[0].parsed_response.VariationSummary.HighestPrice["FormattedPrice"].text
                    }
                }
            }

        except:
            error = {
                'error': 'amazon api exception'
            }
            return json.dumps(error)

    return json.dumps(product_info)
