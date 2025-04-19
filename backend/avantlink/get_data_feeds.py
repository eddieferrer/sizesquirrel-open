import urllib
import datetime
from backend import app
from flask import current_app

def get_data_feeds():
    currentDate = datetime.datetime.today()
    print(currentDate)
    print("Getting Data Feeds...")
    urlOpener = urllib.request.URLopener()
    # BackCountry.com
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246199&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/backcountry_datafeed.xml")
    # BentGate
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246471&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/bentgate_datafeed.xml")
    # Black Diamond Equipment
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=255265&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/blackdiamondequipment_datafeed.xml")
    # CampSaver
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246495&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/campsaver_datafeed.xml")
    # LaSportiva
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=262033&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/lasportiva_datafeed.xml")
    # Outdoor Gear Exchange
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=249021&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/outdoorgearexchange_datafeed.xml")
    # REI
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=247391&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/rei_datafeed.xml")

    print("Done Getting Data Feeds...")