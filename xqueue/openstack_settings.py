from aws_settings import *

# Use OpenStack Swift as the default storage backend
DEFAULT_FILE_STORAGE = 'swift.storage.SwiftStorage'

# OpenStack credentials
SWIFT_AUTH_URL = AUTH_TOKENS.get('SWIFT_AUTH_URL')
SWIFT_AUTH_VERSION = AUTH_TOKENS.get('SWIFT_AUTH_VERSION', 1)
SWIFT_USERNAME = AUTH_TOKENS.get('SWIFT_USERNAME')
SWIFT_KEY = AUTH_TOKENS.get('SWIFT_KEY')
SWIFT_TENANT_NAME = AUTH_TOKENS.get('SWIFT_TENANT_NAME')
SWIFT_TENANT_ID = AUTH_TOKENS.get('SWIFT_TENANT_ID')
SWIFT_USE_TEMP_URLS = AUTH_TOKENS.get('SWIFT_USE_TEMP_URLS', False)
SWIFT_TEMP_URL_KEY = AUTH_TOKENS.get('SWIFT_TEMP_URL_KEY')

if AUTH_TOKENS.get('SWIFT_REGION_NAME'):
    SWIFT_EXTRA_OPTIONS = {'region_name': AUTH_TOKENS['SWIFT_REGION_NAME']}

# Swift container setup
SWIFT_CONTAINER_NAME = UPLOAD_BUCKET
SWIFT_NAME_PREFIX = UPLOAD_PATH_PREFIX
SWIFT_TEMP_URL_DURATION = UPLOAD_URL_EXPIRE
