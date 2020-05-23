import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'dev-database.db')
CACHE_NO_NULL_WARNING = True
DEBUG = True
SECRET_KEY = '42bb78e828c3068641df689467cfe07dcf3594105193f3da'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
FACEBOOK_ID = '944781472301006'
FACEBOOK_SECRET = 'e23be7e727716b5098a8068fb6ec1d1f'
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': FACEBOOK_ID,
        'secret': FACEBOOK_SECRET
    }
}
ROOT_URL = ''

MAIL_SERVER = 'localhost'
MAIL_PORT = 25

# administrator list
ADMINS = ['admin@sizesquirrel.com']

AMAZON_ACCESS_KEY = ''
AMAZON_SECRET_KEY = ''
AMAZON_ASSOC_TAG = ''
AVANT_LINK_AUTH_TOKEN = ''