import urllib
import datetime
from sizeSquirrel import app
from flask import current_app

def get_data_feeds():
    currentDate = datetime.datetime.today()
    print(currentDate)
    print("Getting Data Feeds...")
    urlOpener = urllib.request.URLopener()
    # adidas Outdoor
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=254501&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/adidas_outdoor_datafeed.xml")
    # BackCountry.com
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246199&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/backcountry_datafeed.xml")
    # BentGate
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246471&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/bentgate_datafeed.xml")
    # Black Diamond Equipment
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=255265&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/blackdiamondequipment_datafeed.xml")
    # CampSaver
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246495&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/campsaver_datafeed.xml")
    # Eastern Mountain Sports
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=247395&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/ems_datafeed.xml")
    # Left Lane Sports
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=255397&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/leftlanesports_datafeed.xml")
    # Moosejaw
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=247387&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/moosejaw_datafeed.xml")
    # TODO Mountain Steals
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=259517&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/mountainsteals_datafeed.xml")
    # TODO Outdoor Gear Exchange
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=249021&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/outdoorgearexchange_datafeed.xml")
    # REI
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=247391&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/rei_datafeed.xml")
    # The Clymb
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=255401&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/theclymb_datafeed.xml")
    # TODO US Outdoor Store
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=249137&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/usoutdoorstore_datafeed.xml")
    # LaSportiva
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=262033&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       "sizeSquirrel/datafeeds/lasportiva_datafeed.xml")
    print("Done Getting Data Feeds...")