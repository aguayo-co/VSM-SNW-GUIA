"""
Django settings for vsm_snw project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import ipaddress
import os
import socket

import dj_database_url

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
DEBUG = os.environ.get("DEBUG", "True") == "True"
SECRET_KEY = os.environ.get("SECRET_KEY")
ROOT_URLCONF = "vsm_snw.urls"
WSGI_APPLICATION = "vsm_snw.wsgi.application"

# Application definition
INSTALLED_APPS = [
    "commons",
    "menus",
    "search",
    "forms",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.contrib.settings",
    "wagtail",
    "wagtailmenus",
    "modelcluster",
    "taggit",
    "debug_toolbar",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sass_processor",
    "django_vite",
    "wagtail_tag_manager",
    "wagtail_svg_images",
    "wagtailsvg",
    "generic_chooser",
    "hitcount",
    "wagtail_transfer",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "wagtail_tag_manager.middleware.CookieConsentMiddleware",
    "wagtail_tag_manager.middleware.TagManagerMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail_tag_manager.context_processors.consent_state",
                "django.template.context_processors.i18n",
                "wagtailmenus.context_processors.wagtailmenus",
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {"default": None}

if os.environ.get("DATABASE_URL", None) is not None:
    DATABASES["default"] = dj_database_url.config(default=os.environ["DATABASE_URL"])
    DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql"
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["DATABASE_NAME"],
            "USER": os.environ["DATABASE_USER"],
            "PASSWORD": os.environ["DATABASE_PASSWORD"],
            "HOST": os.environ["DATABASE_HOST"],
            "PORT": os.environ["DATABASE_PORT"],
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "es"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
    "sass_processor.finders.CssFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
    os.path.join(BASE_DIR, "ui"),
    # os.path.join(BASE_DIR, "node_modules"),
]


# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
if DEBUG == False:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# vite
# https://github.com/MrBin99/django-vite
DJANGO_VITE_ASSETS_PATH = os.environ.get(
    "DJANGO_VITE_ASSETS_PATH", os.path.join(PROJECT_DIR, "static/")
)
DJANGO_VITE_DEV_MODE = os.environ.get("DJANGO_VITE_DEV_MODE", "False") == "True"


# Wagtail settings
WAGTAIL_SITE_NAME = "vsm_snw"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html\
if os.environ.get("ELASTIC_SEARCH_URL", None):
    WAGTAILSEARCH_BACKENDS = {
        "default": {
            "BACKEND": "wagtail.search.backends.elasticsearch7",
            "URLS": ["http://es:9200"],
            #     "URLS": [
            #     elastic_url
            #     for elastic_url in os.environ.get(
            #         "ELASTIC_SEARCH_URL", "http://es:9200".split(" ")
            #     )
            # ],
            "INDEX": "wagtail",
            "TIMEOUT": 5,
            "OPTIONS": {},
            "INDEX_SETTINGS": {
                "settings": {
                    "index": {
                        "number_of_shards": 1,
                    },
                    "analysis": {
                        "analyzer": {
                            "default": {"type": "spanish"},
                            "english": {"type": "english"},
                        }
                    },
                }
            },
        }
    }
else:
    WAGTAILSEARCH_BACKENDS = {
        "default": {
            "BACKEND": "wagtail.search.backends.database",
        }
    }

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"


# Allowed hosts
# https://docs.djangoproject.com/en/dev/topics/security/#host-headers-virtual-hosting
if os.environ.get("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(" ")
    CSRF_TRUSTED_ORIGINS = [
        f"https://{host}" for host in os.environ["ALLOWED_HOSTS"].split(" ")
    ]

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [
    ipaddress.ip_network(address)
    for address in os.environ.get("INTERNAL_ADDRESSES", "127.0.0.1").split(" ")
] + [ip[: ip.rfind(".")] + ".1" for ip in ips]

# # SSL Settings.
# # Trust Proxy header and redirect to SSL.
# # https://docs.djangoproject.com/en/dev/ref/middleware/#django.middleware.security.SecurityMiddleware
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL", "False") == "True"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

WAGTAILMENUS_FLAT_MENUS_HANDLE_CHOICES = (("footer_menu", "Footer Menú"),)
WAGTAILMENUS_FLAT_MENU_ITEMS_RELATED_NAME = "custom_flat_menu_items"
WAGTAILMENUS_SECTION_ROOT_DEPTH = 1


# Editors
WAGTAILADMIN_RICH_TEXT_EDITORS = {
    "inline": {
        "WIDGET": "wagtail.admin.rich_text.DraftailRichTextArea",
        "OPTIONS": {
            "features": [
                "bold",
                "italic",
                "underline",
                "mark",
                "superscript",
                "subscript",
                "small",
                "link",
                "document-link",
                "strikethrough",
            ]
        },
    },
    "list": {
        "WIDGET": "wagtail.admin.rich_text.DraftailRichTextArea",
        "OPTIONS": {
            "features": [
                "bold",
                "italic",
                "underline",
                "striketrough",
                "mark",
                "sup",
                "sub",
                "small",
                "link",
                "document-link",
                "ol",
                "ul",
                "h4",
            ]
        },
    },
    "basic": {
        "WIDGET": "wagtail.admin.rich_text.DraftailRichTextArea",
        "OPTIONS": {
            "features": [
                "bold",
                "italic",
                "underline",
                "strikethrough",
                "mark",
                "superscript",
                "subscript",
                "small",
                "ol",
                "ul",
                "link",
                "document-link",
            ]
        },
    },
}

# Sass Processor
# https://github.com/jrief/django-sass-processor
SASS_PROCESSOR_ENABLED = True
SASS_PROCESSOR_ROOT = "ui"
SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(PROJECT_DIR, "ui/"),
    os.path.join(PROJECT_DIR, "ui/sass/"),
    os.path.join(PROJECT_DIR, "node_modules"),
]
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r"^.+\.scss$"
SASS_PRECISION = 8
NODE_NPX_PATH = os.environ.get("NODE_NPX_PATH", None)
NODE_MODULES_PATH = os.path.join(PROJECT_DIR, "node_modules")


# Debug Toolbar
SHOW_DEBUG_TOOLBAR = os.environ.get("SHOW_DEBUG_TOOLBAR", "False") == "True"
if SHOW_DEBUG_TOOLBAR:

    def show_toolbar(request):
        return True

    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}


# Storage
# https://django-storages.readthedocs.io/en/latest/index.html
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
DEFAULT_FILE_STORAGE = os.environ.get(
    "DEFAULT_FILE_STORAGE", "storages.backends.s3boto3.S3Boto3Storage"
)
if DEFAULT_FILE_STORAGE == "storages.backends.s3boto3.S3Boto3Storage":
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_FILE_OVERWRITE = True
    AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", None)
    AWS_QUERYSTRING_EXPIRE = 60 * 60 * 24 * 7  # 1 week
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", None)
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
    if os.environ.get("AWS_STORAGE_BUCKET_NAME", None) is not None:
        AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", None)
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": f"max-age={60 * 60 * 24 * 7 * 4}"  # 4 weeks
    }
    if os.environ.get("AWS_QUERYSTRING_AUTH", None) is not None:
        AWS_QUERYSTRING_AUTH = os.environ.get("AWS_QUERYSTRING_AUTH") == "True"
    if os.environ.get("AWS_LOCATION", None) is not None:
        AWS_LOCATION = os.environ.get("AWS_LOCATION").strip("/") + "/"
    # STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
    SASS_PROCESSOR_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# LoGGING
# Add root console logger with configurable level.
# https://docs.djangoproject.com/en/3.2/topics/logging/#topic-logging-parts-loggers
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": os.getenv("LOG_LEVEL", "WARNING"),
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("LOG_LEVEL", "WARNING"),
    },
    "loggers": {
        "django.db": {
            "handlers": ["console"],
            "level": os.getenv("DB_LOG_LEVEL", "ERROR"),
            "propagate": False,
        },
        "": {
            "handlers": ["console"],
            "level": os.getenv("LOG_LEVEL", "WARNING"),
        },
    },
}

# Wagtail Transfer
WAGTAILTRANSFER_SOURCES = {
    "staging": {
        "BASE_URL": os.environ.get("STAGING_BASE_URL", None),
        "SECRET_KEY": os.environ.get("STAGING_SECRET_KEY", None),
    },
    "production": {
        "BASE_URL": os.environ.get("PRODUCTION_BASE_URL", None),
        "SECRET_KEY": os.environ.get("PRODUCTION_SECRET_KEY", None),
    },
}

WAGTAILTRANSFER_SECRET_KEY = os.environ.get("SECRET_KEY", None)

WAGTAILTRANSFER_UPDATE_RELATED_MODELS = [
    "wagtailadmin.admin",
    "wagtailimages.image",
    "wagtaildocs.document",
    "wagtailredirects.redirect",
    # "commons.degree",
    # "commons.subject",
    # "commons.serie",
]

WAGTAILTRANSFER_NO_FOLLOW_MODELS = [
    # "wagtaildocs.document",
    "wagtailimages.image",
    "wagtailsvg.svg",
    # "commons.subject",
    "commons.degree",
]

WAGTAILTRANSFER_LOOKUP_FIELDS = {
    "taggit.tag": ["slug"],
    "wagtailcore.locale": ["language_code"],
    "contenttypes.contenttype": ["app_label", "model"],
    "auth.permission": ["codename"],
    # "commons.BasePage": ["page_ptr_id"],
}
