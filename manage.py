import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server, Command
from flask_migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(basedir, os.pardir))

os.environ['SETTINGS_FILE'] = os.path.join(basedir, 'dev_settings.py')

from backend import app, db
from backend.avantlink.process_data_feeds import process_data_feeds, item_list, outfile, process_missing_items
from backend.avantlink.get_data_feeds import get_data_feeds
from backend.scripts.plot_user_registrations import plot_user_registrations
from backend.scripts.sanitize_dev_database import sanitize_dev_database
from backend.scripts.set_stats_items import set_stats_items, set_stats_specific_item

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
