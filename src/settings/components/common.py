from decouple import config

SECRET_KEY = config("SECRET_KEY", "BAD_SECRET_KEY_73812732478324783274823")
AUTH_USER_MODEL = "users.User"

PAGINATION_BY = 6
SITE_ID = 1

DEBUG = True
ALLOWED_HOSTS = ["*"]

CSRF_COOKIE_NAME = "XCSRF-Token"

A_P_V = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_PASSWORD_VALIDATORS = config("AUTH_PASSWORD_VALIDATORS", A_P_V)

OPTIMIZED_IMAGE_METHOD = "pillow"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

CORS_ALLOWED_ORIGINS = ['https://api.littleknitsstory.com']
CSRF_TRUSTED_ORIGINS = ['https://api.littleknitsstory.com']
