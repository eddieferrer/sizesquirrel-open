import os
import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

from logging.handlers import RotatingFileHandler
from flask import Flask, current_app
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(basedir, os.pardir))
app = Flask(__name__, static_folder=os.environ['static_folder'], static_url_path=os.environ['static_url_path'], template_folder=os.environ['template_folder'])
            
app.config.from_envvar('SETTINGS_FILE')

if app.debug is not True:
    # All of this is already happening by default!
    sentry_logging = LoggingIntegration(
        level=logging.INFO,        # Capture info and above as breadcrumbs
        event_level=logging.ERROR  # Send errors as events
    )
    sentry_sdk.init(
        dsn="https://2144d22e03f14ef59924331bdb19978b@sentry.io/1157656",
        integrations=[sentry_logging]
    )

    # define the cache config keys, remember that it can be done in a settings file
    app.config['CACHE_TYPE'] = 'simple'

else:
    app.config['CACHE_TYPE'] = 'null'

app.cache = Cache(app)
db = SQLAlchemy(app)
mail = Mail(app)

import sizeSquirrel.views

# if app.debug is not True:
#     file_handler = RotatingFileHandler(
#         '/var/log/sizesquirrel/sizesquirrel_error.log', maxBytes=1024 * 1024 * 100, backupCount=20)
#     file_handler.setLevel(logging.ERROR)
#     formatter = logging.Formatter(
#         "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#     file_handler.setFormatter(formatter)
#     app.logger.addHandler(file_handler)

if __name__ == '__main__':
    # db.create_all()
    app.run()
