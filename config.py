import os, logging
from flask_oauthlib.client import OAuth, session
from secrets import SECRET_GOOGLE_CLIENT_ID, SECRET_GOOGLE_CLIENT_SECRET

basedir = os.path.abspath(os.path.dirname(__file__))

oauth = OAuth()

# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = SECRET_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = SECRET_GOOGLE_CLIENT_SECRET
REDIRECT_URI = '/authorized'  # one of the Redirect URIs from Google APIs console

google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)
