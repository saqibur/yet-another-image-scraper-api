import os
from pathlib import Path

from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", None)

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(",")

DEFAULT_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.messages",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_yasg",
]

SELF_APPS = [
    "apps.core",
    "apps.image",
    "apps.scraper",
    "apps.seed",
    "apps.user",
]

INSTALLED_APPS = DEFAULT_APPS + SELF_APPS + THIRD_PARTY_APPS

AUTH_USER_MODEL = "user.User"

DEFAULT_MIDDLEWARES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

THIRD_PARTY_MIDDLEWARES = []

SELF_MIDDLEWARES = []

MIDDLEWARE = DEFAULT_MIDDLEWARES + THIRD_PARTY_MIDDLEWARES + SELF_MIDDLEWARES

TOKEN_EXPIRED_AFTER_SECONDS = config("TOKEN_EXPIRED_AFTER_SECONDS", 8 * 60 * 60, cast=int)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "TEST_REQUEST_RENDERER_CLASSES": (
        "rest_framework.renderers.MultiPartRenderer",
        "rest_framework.renderers.JSONRenderer",
    ),
}

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": config("DB_NAME"),
    }
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": None,
    "USE_SESSION_AUTH": False,
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

LANGUAGE_CODE = "en-us"

# Security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Django APScheduler Settings
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds
FETCH_URLS_FROM_SCRAPED_IMAGES_JOB_INTERVAL = "*/5"  # Every 5 minutes

WAIT_PERIOD_BETWEEN_IMAGE_DOWNLOADS = 2  # In seconds
