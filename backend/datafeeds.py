import xmltodict
from collections import OrderedDict
from backend import app

# Adding and removing a datafeed should be done in this file and in 
# frontend/components/ItemListFiltersServer.vue

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
        'retailer_short_name': 'backcountry',
        'avantlink_id': '246199',
    },
    {
        'datafeed': get_datafeed('bentgate'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/11741.png',
        'retailer_name': 'Bent Gate',
        'retailer_short_name': 'bentgate',
        'avantlink_id': '246471',
    },
    {
        'datafeed': get_datafeed('blackdiamondequipment'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/16109.png',
        'retailer_name': 'Black Diamond Equipment',
        'retailer_short_name': 'blackdiamondequipment',
        'avantlink_id': '327229',
    },
    {
        'datafeed': get_datafeed('campsaver'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/10008.png',
        'retailer_name': 'Camp Saver',
        'retailer_short_name': 'campsaver',
        'avantlink_id': '246495',
    },
    {
        'datafeed': get_datafeed('lasportiva'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/16709.png',
        'retailer_name': 'La Sportiva',
        'retailer_short_name': 'lasportiva',
        'avantlink_id': '262033',
    },
    {
        'datafeed': get_datafeed('outdoorgearexchange'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/14967.png',
        'retailer_name': 'Outdoor Gear Exchange',
        'retailer_short_name': 'outdoorgearexchange',
        'avantlink_id': '249021',
    },
    {
        'datafeed': get_datafeed('rei'),
        'retailer_logo': 'https://static.avantlink.com/merchant-logos/10248.png',
        'retailer_name': 'REI',
        'retailer_short_name': 'rei',
        'avantlink_id': '247391',
    }
]