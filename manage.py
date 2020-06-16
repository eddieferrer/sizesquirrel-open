import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server, Command
from flask_migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(basedir, os.pardir))

os.environ['SETTINGS_FILE'] = os.path.join(basedir, 'dev_settings.py')
os.environ['static_folder'] = "./frontend/dist/static"
os.environ['static_url_path'] = "/fakepath/" # overwrite the flask path, any path that doesnt exist will do
os.environ['template_folder'] = "./frontend/dist"

import dev_settings

from sizeSquirrel import app, db
from sizeSquirrel.avantlink.process_data_feeds import process_data_feeds, item_list, outfile, process_missing_items
from sizeSquirrel.avantlink.get_data_feeds import get_data_feeds
from sizeSquirrel.scripts.plot_user_registrations import plot_user_registrations
from sizeSquirrel.scripts.sanitize_dev_database import sanitize_dev_database

from sizeSquirrel.scripts.set_stats_items import set_stats_items, set_stats_specific_item

app.SQLALCHEMY_DATABASE_URI = dev_settings.SQLALCHEMY_DATABASE_URI
app.DEBUG = dev_settings.DEBUG
app.SECRET_KEY = dev_settings.SECRET_KEY
app.SQLALCHEMY_COMMIT_ON_TEARDOWN = dev_settings.SQLALCHEMY_COMMIT_ON_TEARDOWN
app.OAUTH_CREDENTIALS = {
    'facebook': {
        'id': dev_settings.FACEBOOK_ID,
        'secret': dev_settings.FACEBOOK_ID
    }
}
app.ROOT_URL = dev_settings.ROOT_URL
app.AVANT_LINK_AUTH_TOKEN = dev_settings.AVANT_LINK_AUTH_TOKEN
app.DATAFEED_PATH = dev_settings.DATAFEED_PATH


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host='0.0.0.0', port='5000'))

@manager.command
def get_feeds():
    get_data_feeds()

@manager.command
def make_item_list():
    item_list()

@manager.command
def make_outfile():
    outfile()

@manager.option('-f', '--feed')
def process_feeds(feed):
    process_data_feeds(feed)

@manager.option('-f', '--feed')
def process_missing(feed):
    process_missing_items(feed)

@manager.option('-i', '--item')
def set_stats_item(item):
    set_stats_specific_item(item)

@manager.command
def user_registrations():
    plot_user_registrations()

@manager.command
def set_stats():
    set_stats_items()

@manager.command
def sanitize_database():
    sanitize_dev_database()

if __name__ == '__main__':
    manager.run()
