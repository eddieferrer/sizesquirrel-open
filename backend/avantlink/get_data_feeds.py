import urllib
import datetime
import requests
from backend.models import CONSTANT_BRANDS
from flask import current_app
from backend.datafeeds import DATA_FEED_INFO_ARRAY


def get_data_feeds():
    get_avantlink_feeds()
    get_impact_feeds()

def get_avantlink_feeds():
    currentDate = datetime.datetime.today()
    print(currentDate)
    print("Getting Avantlink Data Feeds...")
    urlOpener = urllib.request.URLopener()

    for feedinfo in DATA_FEED_INFO_ARRAY:
        # Get only config objects that have the key 'avantlink_id'
        if 'avantlink_id' not in feedinfo:
            continue
        # Get the datafeed for each retailer
        urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=" + feedinfo['avantlink_id'] + "&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                           current_app.config['DATAFEED_PATH'] + "/" + feedinfo['retailer_short_name'] + "_datafeed.xml")

    print("Done Getting Avantlink Data Feeds...")

def capitalize_first_letter_of_every_word(text):
  return ' '.join(word.capitalize() for word in text.split())

def get_impact_feeds():
    print("Getting Impact Data Feeds...")

    # Combine and comma separate all brands in 
    # CONSTANT_BRANDS and slugify them
    # to be used in the query string
    brands = []
    for brand in CONSTANT_BRANDS:
        brands.append('"' + capitalize_first_letter_of_every_word(brand) + '"')
    brands = [brand.replace(' ', '%20') for brand in brands]

    # Join the brands with commas
    brands = ','.join(brands)

    print("Brands: " + brands)

    headers = {
        'Accept': 'application/json',
    }

    for feedinfo in DATA_FEED_INFO_ARRAY:
        # Get only config objects that have the key 'impact_id'
        if 'impact_id' not in feedinfo:
            continue
        requestUrl = 'https://api.impact.com/Mediapartners/' + current_app.config['IMPACT_ACCOUNT_SID'] + '/Catalogs/' + feedinfo['impact_id'] + '/Items?Query=ManufacturerIN('+ brands + ')ANDStockAvailability=\"InStock\"&Keyword=\"climb\"&PageSize=1000'

        response = requests.get(
            requestUrl,
            headers=headers, 
            auth=(current_app.config['IMPACT_ACCOUNT_SID'], current_app.config['IMPACT_AUTH_TOKEN'])
        )

        # save file
        with open(current_app.config['DATAFEED_PATH'] + '/' + feedinfo['retailer_short_name'] + '_impact.json', 'wb') as f:
            f.write(response.content)

        try:
            jsonData = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON")  

        # get additional pages
        
        if jsonData["@numpages"] is not None and int(jsonData["@numpages"]) > 1:
            for page in range(2, int(jsonData["@numpages"]) + 1):
                response = requests.get(requestUrl + '&Page=' + str(page),
                    headers=headers, 
                    auth=(current_app.config['IMPACT_ACCOUNT_SID'], current_app.config['IMPACT_AUTH_TOKEN'])
                )
                # save file
                with open(current_app.config['DATAFEED_PATH'] + '/' + feedinfo['retailer_short_name'] + '_impact.json', 'ab') as f:
                    f.write(response.content)
    print("Done Getting Impact Data Feeds...")
