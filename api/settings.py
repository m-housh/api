# -*- coding: utf-8 -*-

import os
import api_defs

# Get mongo setup stuff from the environment or use the defaults
# if not present.
MONGO_HOST = os.environ.get('MONGO_HOST', 'mongo')
MONGO_PORT = os.environ.get('MONGO_PORT', '27017')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'api')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'api')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'password')
MONGO_AUTHDBNAME = os.environ.get('MONGO_AUTHDBNAME', 'api')

# build the mongo uri
MONGO_URI = 'mongodb://{0}:{1}@{2}/{3}'.format(
        MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST, MONGO_DBNAME)

# get debug status from the environment.
_debug = os.environ.get('DEBUG')
if _debug == 'true' or _debug == 'True' or _debug == 'TRUE' or _debug == 0:
    DEBUG = True


# allow full range of CRUD operations on resources and items
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']


# disable HATEOAS
HATEOAS = False


# We want the whole document back with POST/PATCH/PUT responses.
BANDWIDTH_SAVER = False

CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Enable server information at the API homepage
INFO = '_info'

# prefix all routes with /api
URL_PREFIX = 'api'

# load the domain from api_defs
DOMAIN = api_defs.domain()
