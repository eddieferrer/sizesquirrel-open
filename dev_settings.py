import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'dev-database.db')
CACHE_NO_NULL_WARNING = True
DEBUG = True
SECRET_KEY = '42bb78e828c3068641df689467cfe07dcf3594105193f3da'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
ROOT_URL = ''

MAIL_SERVER = 'localhost'
MAIL_PORT = 25

# administrator list
ADMINS = ['admin@sizesquirrel.com']

AVANT_LINK_AUTH_TOKEN = ''

DATAFEED_PATH = 'backend/sample_datafeeds'
SENTRY_DSN = ''