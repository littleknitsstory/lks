from decouple import config

EMAIL_HOST = config("EMAIL_HOST", "")
EMAIL_PORT = config("EMAIL_PORT", "")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", "")
SENDGRID_API_KEY = config("SENDGRID_API_KEY", "")
