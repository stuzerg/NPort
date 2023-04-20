"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os, logging
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3pcq5lz4urwe06m739k%r_zxkat$ba(j4l_lp2oxo&qq9c&7^x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'news_paper.apps.NewsPaperConfig',
    'django_filters',

    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',

    'django_apscheduler',

]

DEFAULT_FROM_EMAIL = ''
SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


LOGIN_URL = '/accounts/login/' #"sign/login/"
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465
EMAIL_HOST_USER = os.environ.get('USER_name')  # ваше имя пользователя
EMAIL_HOST_PASSWORD = os.environ.get('USER_pass')  # пароль от почты
EMAIL_USE_SSL = True

ADMINS = [
    ('stut', 'stutzerg@gmail.com'),
    # список всех админов в формате ('имя', 'их почта')
]
SERVER_EMAIL = os.environ.get('USER_name') + '@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

SITE_URL = 'localhost:8000'

CELERY_BROKER_URL = 'redis://default:R8tugt67rE9m2ooLbBtdVMHfcfYyvIXl@redis-19181.c299.asia-northeast1-1.gce.cloud.redislabs.com:19181'
CELERY_RESULT_BACKEND = 'redis://default:R8tugt67rE9m2ooLbBtdVMHfcfYyvIXl@redis-19181.c299.asia-northeast1-1.gce.cloud.redislabs.com:19181'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 'style' : '{',
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'simple_withpathname': {
            'format': '%(asctime)s %(levelname)s  %(message)s путь %(pathname)s'
        },
        'simple_withpathname_error': {
            'format': '%(asctime)s %(levelname)s %(exc_info)s %(message)s путь  %(pathname)s'
        },

        'log_format1': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'},
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'},
                },
    'handlers': {
        'console1': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'rich.logging.RichHandler', #pip install rich
            'formatter': 'simple'
        },
        'console2': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'rich.logging.RichHandler', #pip install rich
            'formatter': 'simple_withpathname'
        },

        'console3': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'rich.logging.RichHandler', #pip install rich
            'formatter': 'simple_withpathname_error'
        },


        'log_to_general': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'filename': 'logs/General.log' ,
            'formatter': 'log_format1'
        },

        'log_to_errors': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'filename': 'logs/Errors.log' ,
            'formatter': 'simple_withpathname_error'
        },

        'log_to_security': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',

            'filters': ['require_debug_true'],
            'filename': 'logs/Security.log' ,
            'formatter': 'log_format1'
        },



        'mail_admins': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'formatter': 'simple_withpathname',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console1', 'console2', 'console3',  'log_to_general', ],
            'level': 'DEBUG',
            'propagate': True
        },

        'django.request': {
            'handlers': ['log_to_errors', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.server': {
            'handlers': ['log_to_errors', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.template': {
            'handlers': ['log_to_errors',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['log_to_errors',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['log_to_security' ],
            'level': 'DEBUG',
            'propagate': True,
        }

    }
}
