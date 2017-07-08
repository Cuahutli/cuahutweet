from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['social.cuahutli.com', 'www.social.cuahutli.com']

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # will not be server, long term storage
    os.path.join(BASE_DIR, "static"),
]

#add root STATICS
# will be served
STATIC_ROOT =  os.path.join(os.path.dirname(BASE_DIR), "static-cdn")#CDN
