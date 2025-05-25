import xmltodict
import json
from collections import OrderedDict
from backend import app

# Adding and removing a datafeed should be done in this file and in 
# frontend/components/ItemListFiltersServer.vue
# batch_arguments.py
def load_avantlink_feed(retailer):
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

def load_impact_feed(retailer):
    try: 
        with open(app.config['ROOT_URL'] + app.config['DATAFEED_PATH'] + '/' + retailer+'_impact.json') as fd:
            obj = json.loads(fd.read())

        obj = obj["Items"]

        # Duplicate and rename keys on every item so that it conforms with the avantlink key namings
        # and so that we can use the same template for both feeds
        for item in obj:
            item["Brand_Name"] = item["Manufacturer"]
            item["Buy_Link"] = item["Url"]
            item["Image_URL"] = item["ImageUrl"]
            item["Long_Description"] = item["Description"]
            item["Product_Name"] = item["Name"]
            item["Retail_Price"] = item["OriginalPrice"]
            item["Sale_Price"] =item["CurrentPrice"]
            item["SKU"] = item["CatalogItemId"]
            item["Thumb_URL"] = ""
            item["Variants"] = ""
        return obj
    except:
        return [] 
    
DATA_FEED_INFO_ARRAY = [
    {
        'datafeed': load_impact_feed('backcountry'),
        'retailer_logo': 'https://a.impactradius-go.com/display-ad/5311-786378',
        'retailer_name': 'Backcountry',
        'retailer_short_name': 'backcountry',
        'impact_id': '15874',
    },
    {
        'datafeed': load_avantlink_feed('bentgate'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/11741.png',
        'retailer_name': 'Bent Gate',
        'retailer_short_name': 'bentgate',
        'avantlink_id': '246471',
    },
    {
        'datafeed': load_avantlink_feed('blackdiamondequipment'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/16109.png',
        'retailer_name': 'Black Diamond Equipment',
        'retailer_short_name': 'blackdiamondequipment',
        'avantlink_id': '327229',
    },
    {
        'datafeed': load_avantlink_feed('campsaver'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/10008.png',
        'retailer_name': 'Camp Saver',
        'retailer_short_name': 'campsaver',
        'avantlink_id': '246495',
    },
    {
        'datafeed': load_avantlink_feed('lasportiva'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/16709.png',
        'retailer_name': 'La Sportiva',
        'retailer_short_name': 'lasportiva',
        'avantlink_id': '262033',
    },
    {
        'datafeed': load_avantlink_feed('outdoorgearexchange'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/14967.png',
        'retailer_name': 'Outdoor Gear Exchange',
        'retailer_short_name': 'outdoorgearexchange',
        'avantlink_id': '249021',
    },
    {
        'datafeed': load_impact_feed('rei'),
        'retailer_logo': 'https://a.impactradius-go.com/display-ad/17195-1867507',
        'retailer_name': 'REI',
        'retailer_short_name': 'rei',
        'impact_id': '11020',
    },
    {
        'datafeed': load_impact_feed('steepandcheap'),
        'retailer_logo': 'https://a.impactradius-go.com/display-ad/5418-389917',
        'retailer_name': 'Steep And Cheap',
        'retailer_short_name': 'steepandcheap',
        'impact_id': '2394',
    }
]