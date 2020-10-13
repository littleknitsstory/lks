import sentry_sdk

SITE_NAME = "127.0.0.1:8000"
DEBUG = True
ROBOTS_USE_SITEMAP = False
ROBOTS_SITEMAP_VIEW_NAME = "sitemap"

ROBOTS_USE_HOST = False
ROBOTS_USE_SCHEME_IN_HOST = False

# off sentry
sentry_sdk.init()
