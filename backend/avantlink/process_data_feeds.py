import xmltodict
import pickle
import datetime
import json

from collections import OrderedDict
from backend import app, db
from backend.models import Item, CONSTANT_BRANDS
from backend.emails import send_email

from backend.utils import list_all_items, match_strings
from flask import render_template, current_app

def get_datafeed(retailer):
    try: 
        with open(app.config['ROOT_URL'] + app.config['DATAFEED_PATH'] + '/' + retailer+'_datafeed.xml') as fd:
            obj = xmltodict.parse(fd.read())

        obj = obj["Products"]

        if obj:
            root_elements = obj["Product"] if type(
                obj) == OrderedDict else [obj["Product"]]
        else:
            root_elements = []

        if type(root_elements) == OrderedDict:
            root_elements = [root_elements]
        # Above step ensures that root_elements is always a list
        # for element in root_elements:
        #     print element["SKU"]
        return root_elements
    except:
        return []        


DATA_FEED_INFO_ARRAY = [
    {
        'datafeed': get_datafeed('backcountry'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/10060.png',
        'retailer_name': 'Backcountry',
        'retailer_short_name': 'backcountry'
    },
    {
        'datafeed': get_datafeed('bentgate'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/11741.png',
        'retailer_name': 'Bent Gate',
        'retailer_short_name': 'bentgate'
    },
    {
        'datafeed': get_datafeed('blackdiamondequipment'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/16109.png',
        'retailer_name': 'Black Diamond Equipment',
        'retailer_short_name': 'blackdiamondequipment'
    },
    {
        'datafeed': get_datafeed('campsaver'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/10008.png',
        'retailer_name': 'Camp Saver',
        'retailer_short_name': 'campsaver'
    },
    {
        'datafeed': get_datafeed('lasportiva'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/16709.png',
        'retailer_name': 'La Sportiva',
        'retailer_short_name': 'lasportiva'
    },
    {
        'datafeed': get_datafeed('outdoorgearexchange'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/14967.png',
        'retailer_name': 'Outdoor Gear Exchange',
        'retailer_short_name': 'outdoorgearexchange'
    },
    {
        'datafeed': get_datafeed('rei'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/10248.png',
        'retailer_name': 'REI',
        'retailer_short_name': 'rei'
    }
]

def item_list():
    raw_items = list_all_items()
    for item in raw_items:
        item["datafeeds"] = []
    with open(app.config['ROOT_URL'] + 'itemslist', 'wb') as fp:
        pickle.dump(raw_items, fp, protocol=-1)

def outfile():
    print("Creating Outfile...")
    with open(current_app.config['ROOT_URL'] + 'itemslist', 'rb') as fp:
        raw_items = pickle.load(fp)
    items_filtered = []
    for item in raw_items:
        if item.get('datafeeds'):
            sorted_datafeeds = sorted(
                item["datafeeds"], key=lambda k: float(k['Product']['Sale_Price']))
            item["datafeeds"] = sorted_datafeeds
            item_in_db = Item.query.filter_by(id=item["id"]).first()
            if item_in_db:
                if "Thumb_URL" in item["datafeeds"][0]["Product"]:
                    item_in_db.small_image_url = item["datafeeds"][0]["Product"]["Thumb_URL"]
                else:
                    if "Image_URL" in item["datafeeds"][0]["Product"]:
                        item_in_db.small_image_url = item["datafeeds"][0]["Product"]["Image_URL"]
                    else:
                        item_in_db.small_image_url = ""

                if "Image_URL" in item["datafeeds"][0]["Product"]:
                    item_in_db.medium_image_url = item["datafeeds"][0]["Product"]["Image_URL"]
                else:
                    item_in_db.medium_image_url = ""
                item_in_db.thumbnail_cache = datetime.datetime.utcnow()
                db.session.commit()

            seq = [float(x['Product']['Sale_Price'])
                   for x in item["datafeeds"]]
            seq_percent = [float(x['Percent_Off']) for x in item["datafeeds"]]

            item['lowest_sale_price'] = min(seq)
            item['highest_sale_price'] = max(seq)
            item['percent_off'] = max(seq_percent)

            items_filtered.append(item)

    with open(app.config['ROOT_URL'] + 'outfile', 'wb') as fp:
        pickle.dump(items_filtered, fp, protocol=-1)

def process_data_feeds(target_feed, sendDiscountItems = False, sendMissingItems = False):
    print("-" * 25)
    print("Processing Feed: " + target_feed)
    with open(current_app.config['ROOT_URL'] + 'itemslist', 'rb') as fp:
        raw_items = pickle.load(fp)

    target_feed = [feed for feed in DATA_FEED_INFO_ARRAY if feed['retailer_short_name'] == target_feed]

    feed = target_feed[0]
    feed = clean_up_feed(feed)
    print("Number of products: " + str(len(feed["datafeed"])))

    for product in feed["datafeed"]:
        for item in raw_items:  
            # print feed["retailer_name"]
            # print product["Product_Name"]
            # print product["Brand_Name"]
            # print type(product["Brand_Name"])
            if match_strings(product["Product_Name"], product["Brand_Name"], item):
                # print "Matched"
                # print product["Product_Name"]
                # print product["Brand_Name"]
                # print "________________"

                product = clean_product_list(product)

                datafeed_product = dict(product)

                percent_off = (float(datafeed_product["Retail_Price"]) - float(
                    datafeed_product["Sale_Price"])) * 100 / float(datafeed_product["Retail_Price"])

                # special code for feeds that have 2 entries for same product
                productAlreadyAdded = False
                
                for data_feed_info in item["datafeeds"]:
                    if isSameProduct(data_feed_info, product, feed["retailer_name"]):
                            productAlreadyAdded = True

                # end special code for feeds that have 2 entries for same product

                if productAlreadyAdded is False:
                    item["datafeeds"].append({
                        'Product': json.loads(json.dumps(product)),
                        'Retailer_Name': feed["retailer_name"],
                        'Retailer_Logo': feed["retailer_logo"],
                        'Percent_Off': int(round(percent_off))
                    })
                product["SSMatch"] = True

    # count products in datafeed where product["SSMatch"] is True
    matchedProducts = [product for product in feed["datafeed"] if product.get("SSMatch") == True]
    print ("Matched products: " + str(len(matchedProducts)))

    # Log problem items
    for item in raw_items:  
        if item.get('datafeeds') is not None:
            # get datafeeds for this retailer
            datafeeds = [datafeed for datafeed in item["datafeeds"] if datafeed['Retailer_Name'] == feed["retailer_name"]]
            if len(datafeeds) > 1:
                print(feed["retailer_name"] + "-- Problem Item: " + item["model"] + " - " + str(len(datafeeds)))
    

    with open(app.config['ROOT_URL'] + 'itemslist', 'wb') as fp:
        pickle.dump(raw_items, fp, protocol=-1)
    print("Finished Processing Feed")

    if sendDiscountItems is True:
        print("Sending Discount Items")
        send_admin_discount_items(feed)

    if sendMissingItems is True:
        print("Sending Missing Items")
        send_admin_missing_items(feed)

def send_admin_discount_items(feed):
    # discount items
    discount_items = []

    for product in feed["datafeed"]:
        if product.get('SSMatch') is not None:
            datafeed_product = dict(product)
            percent_off = (float(datafeed_product["Retail_Price"]) - float(
                datafeed_product["Sale_Price"])) * 100 / float(datafeed_product["Retail_Price"])
            if percent_off > 30:
                if "Variants" in product and product["Variants"] is not None:
                    def isFloat(param):
                        try:
                            float(param)
                            return True
                        except:
                            return False
                    # print feed["retailer_name"]
                    # print product["Product_Name"]
                    # print product["Variants"]
                    # print len(product["Variants"])
                    product["Variants"] = [
                        w.replace(' ', '') for w in product["Variants"]]
                    product["Variants"] = [
                        w.replace('EU', '') for w in product["Variants"]]
                    product["Variants"] = [
                        w.replace('US', '') for w in product["Variants"]]
                    product["Variants"] = [
                        w.replace('/', '') for w in product["Variants"]]
                    product["Variants"] = [
                        w.replace('UK', '') for w in product["Variants"]]
                    product["Variants"] = [
                        s for s in product["Variants"] if isFloat(s)]
                    product["Variants"] = [
                        s for s in product["Variants"] if 6 <= float(s) <= 12 or 38 <= float(s) <= 44]

                    if len(product["Variants"]) > 5:
                        # print product["Product_Name"]
                        # print product["Variants"]
                        # print any(
                        #     6 <= float(size) <= 12 for size in product["Variants"])
                        discount_items.append({
                            'Product_Name': product["Product_Name"],
                            'Brand_Name': product["Brand_Name"],
                            'Retailer_Name': feed["retailer_name"],
                            'Percent_Off': int(round(percent_off)),
                            'Variants': product["Variants"],
                            'Sale_Price': product["Sale_Price"],
                            'Buy_Link': product["Buy_Link"]
                        })
    emailSubject = "Discount Items - " + feed["retailer_name"] + " - " +str(len(discount_items))
    if app.debug is not True and len(discount_items) > 0:
        send_email(emailSubject,
                   current_app.config['ADMINS'][0],
                   [current_app.config['ADMINS'][0]],
                   render_template("emails/admin_discount_items.txt", discount_items=discount_items,
                                   time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M")),
                   render_template("emails/admin_discount_items.html", discount_items=discount_items, time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M")))

def send_process_log():
    # send process log to admin
    try:
        with open('/srv/www/sizesquirrel/logs/process_cron_log', 'r') as file:
            contents = file.read()
    except FileNotFoundError:
         print(f"Error: File not found: /srv/www/sizesquirrel/logs/process_cron_log")
         return
    
    emailSubject = "Admin process log"
    if app.debug is not True:
        send_email(emailSubject,
                   current_app.config['ADMINS'][0],
                   [current_app.config['ADMINS'][0]],
                   render_template("emails/admin_discount_items.txt", contents=contents,
                                   time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M")),
                   render_template("emails/admin_discount_items.html", contents=contents, time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M")))

def send_admin_missing_items(feed):
    # make a list of missing items and send to admin
    missing_items = []
    missing_brands = []

    for product in feed["datafeed"]:
        if product.get('SSMatch') is None:
            # print product["Product_Name"]
            # print product["Brand_Name"]
            # print feed["retailer_name"]
            if product["Brand_Name"]: 
                if product["Brand_Name"].lower() in CONSTANT_BRANDS:
                    missing_items.append({
                        'Product_Name': product["Product_Name"],
                        'Brand_Name': product["Brand_Name"],
                        'Retailer_Name': feed["retailer_name"]
                    })
                else:
                    if product["Brand_Name"] not in missing_brands:
                        missing_brands.append(product["Brand_Name"])

    emailSubject = "Missing Items - " + feed["retailer_name"] + " - " +str(len(missing_items))
    if app.debug is not True and len(missing_items) > 0:
        send_email(emailSubject,
                   current_app.config['ADMINS'][0],
                   [current_app.config['ADMINS'][0]],
                   render_template("emails/admin_missing_items.txt", missing_items=missing_items,
                                   missing_brands=missing_brands, time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M")),
                   render_template("emails/admin_missing_items.html", missing_items=missing_items, missing_brands=missing_brands, time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M")))

def clean_product_list(product):
    new_Product_Name = None
    new_Brand_Name = None
    new_Buy_Link = None
    new_Retail_Price = None
    new_SKU = None
    new_Sale_Price = None
    new_Product_Size = None
    new_Thumb_URL = None
    new_Image_URL = None
    new_Variants = None
    new_Long_Description = None


    # lets remove most of the keys in datafeed
    if "Brand_Name" in product:
        new_Brand_Name = product["Brand_Name"]
    if "Product_Name" in product:
        new_Product_Name = product["Product_Name"]
    if "Buy_Link" in product:
        new_Buy_Link = product["Buy_Link"]
    if "Retail_Price" in product:
        new_Retail_Price = product["Retail_Price"]
    if "SKU" in product:
        new_SKU = product["SKU"]
    if "Sale_Price" in product:
        new_Sale_Price = product["Sale_Price"]
    if "Product_Size" in product:
        new_Product_Size = product["Product_Size"]
    if "Thumb_URL" in product:
        new_Thumb_URL = product["Thumb_URL"]
    if "Image_URL" in product:
        new_Image_URL = product["Image_URL"]
    if "Long_Description" in product:
        new_Long_Description = product["Long_Description"]
    if "Extended_Xml_Attributes" in product and product["Extended_Xml_Attributes"] is not None:
        if "variants" in product["Extended_Xml_Attributes"] and product["Extended_Xml_Attributes"]["variants"] is not None:
            tempArray = []
            # print product["Extended_Xml_Attributes"]["variants"]["variant"]
            for x in product["Extended_Xml_Attributes"]["variants"]["variant"]:
                # print type(x)
                if isinstance(x, dict) and "size" in x:
                    # print x["size"]
                    # for variantInfo in x:
                    # print variantInfo
                    tempArray.append(x["size"])
                    new_Variants = tempArray
    product.clear()

    if new_Brand_Name is not None:
        product["Brand_Name"] = new_Brand_Name
    if new_Product_Name is not None:
        product["Product_Name"] = new_Product_Name
    if new_Buy_Link is not None:
        product["Buy_Link"] = new_Buy_Link
    if new_Retail_Price is not None:
        product["Retail_Price"] = new_Retail_Price
    if new_SKU is not None:
        product["SKU"] = new_SKU
    if new_Sale_Price is not None:
        product["Sale_Price"] = new_Sale_Price
    if new_Product_Size is not None:
        product["Product_Size"] = new_Product_Size
    if new_Thumb_URL is not None:
        product["Thumb_URL"] = new_Thumb_URL
    if new_Image_URL is not None:
        product["Image_URL"] = new_Image_URL
    if new_Long_Description is not None:
        product["Long_Description"] = new_Long_Description
    if new_Variants is not None:
        product["Variants"] = new_Variants

    return product

def clean_up_feed(feed):
    # takes in a raw data feed and cleans it up
    if feed["retailer_short_name"] == 'blackdiamondequipment':
        for product in feed["datafeed"][:]:
            # fix missing brand name in BD feed
            product["Brand_Name"] = 'Black Diamond'
            # remove non climbing items
            if "Climbing" not in product["Product_Name"] and \
                "climbing" not in product["Product_Name"]:
                feed["datafeed"].remove(product)

    if feed["retailer_short_name"] == 'lasportiva':
        for product in feed["datafeed"][:]:
            # fix missing brand name in La Sportiva feed
            product["Brand_Name"] = 'La Sportiva'
            # remove non climbing items
            if "Long_Description" in product and \
                "Climbing" not in product["Long_Description"] and \
                "climbing" not in product["Long_Description"] and \
                "CLIMBING" not in product["Long_Description"]:
                feed["datafeed"].remove(product)

    if feed["retailer_name"] == 'rei':
        for product in feed["datafeed"]:
            # REI messed up their datafeed, including 2 properties BrandName per product, this hack fixes that
            if type(product["Brand_Name"]) == list:
                product["Brand_Name"] = ''.join(
                    filter(None, product["Brand_Name"]))

    return feed
    
# Function for determining if 2 properties are referring to the same product
# itemDataFeedEntry is the entry on the sizesquirrel item
# dataFeedProduct is the entry on the datafeed
def isSameProduct(itemDataFeedEntry, dataFeedProduct, retailerName):
    sku1 = itemDataFeedEntry["Product"]["SKU"]
    sku2 = dataFeedProduct["SKU"]
    
    if itemDataFeedEntry["Retailer_Name"] == retailerName and \
        itemDataFeedEntry["Product"]["Brand_Name"] == dataFeedProduct["Brand_Name"]:

        if sku1 == sku2:
            return True
            
        if retailerName == 'Backcountry':
            if sku1[0:7] == sku2[0:7]:
                return True
            
        elif retailerName == 'Black Diamond Equipment':
            if sku1[0:10] == sku2[0:10]:
                return True

        elif retailerName == 'La Sportiva':
            if sku1[0:7] == sku2[0:7]:
                return True
            
        elif retailerName == 'Outdoor Gear Exchange':
            # 1 product with unique sku per size
            if itemDataFeedEntry["Product"]["Sale_Price"] == dataFeedProduct["Sale_Price"] and \
                itemDataFeedEntry["Product"]["Retail_Price"] == dataFeedProduct["Retail_Price"] and \
                itemDataFeedEntry["Product"]["SKU"] != dataFeedProduct["SKU"] and \
                itemDataFeedEntry["Product"]["Long_Description"] == dataFeedProduct["Long_Description"]:
                return True

        elif retailerName == 'Bent Gate' or retailerName == 'Camp Saver' or retailerName == 'REI': 
            return True
    return False