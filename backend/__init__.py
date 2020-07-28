import os
import logging
import sentry_sdk

from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from logging.handlers import RotatingFileHandler
from flask import Flask, current_app
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(basedir, os.pardir))

app = Flask(__name__, static_folder=None, static_url_path=None, template_folder="../frontend/dist")
            
app.config.from_envvar('SETTINGS_FILE')

if app.debug is not True:
    # Initialize Sentry
    sentry_logging = LoggingIntegration(
        level=logging.INFO,        # Capture info and above as breadcrumbs
        event_level=logging.ERROR  # Send errors as events
    )
    sentry_sdk.init(
        dsn=app.config['SENTRY_DSN'],
        integrations=[sentry_logging, FlaskIntegration(), SqlalchemyIntegration()]
    )

# Initialize Cache
if app.debug is not True:
    app.config['CACHE_TYPE'] = 'simple'
else:
    app.config['CACHE_TYPE'] = 'null'

app.cache = Cache(app)
db = SQLAlchemy(app)
mail = Mail(app)

import backend.views

if __name__ == '__main__':
    app.run()
