"""
Django settings for vsm_snw project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import ipaddress

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "commons",
    "menus",
    "search",
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
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "vsm_snw.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "vsm_snw.wsgi.application"


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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
    os.path.join(BASE_DIR, "ui"),
    os.path.join(BASE_DIR, "node_modules"),
]


# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "vsm_snw"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
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

# Internal Ips
import socket  # only if you haven't already imported this
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [
    ipaddress.ip_network(address)
    for address in os.environ.get("INTERNAL_ADDRESSES", "127.0.0.1").split(" ")
] + [ip[: ip.rfind(".")] + ".1" for ip in ips]

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
