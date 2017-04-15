import os, logging
from db_config import *
from flask_oauthlib.client import OAuth, session
from secrets import SECRET_GOOGLE_CLIENT_ID, SECRET_GOOGLE_CLIENT_SECRET, MY_SECRET_KEY

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + '/' + DB_NAME
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = MY_SECRET_KEY
CSRF_ENABLED = True
oauth = OAuth()

# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = SECRET_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = SECRET_GOOGLE_CLIENT_SECRET
REDIRECT_URI = '/authorized'  # one of the Redirect URIs from Google APIs console

google = oauth.remote_app(
    'google',
    consumer_key=GOOGLE_CLIENT_ID,
    consumer_secret=GOOGLE_CLIENT_SECRET,
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)
