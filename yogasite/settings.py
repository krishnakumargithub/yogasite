"""
Django settings for yogasite project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""







# Application definition



import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l4g8%jd-n_68gx95=4(+6^79z(41l#f3o+x^v6p_$9w)fyyria'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Application definition






INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yogaclubiiita',
]





ROOT_URLCONF = 'yogasite.urls'

WSGI_APPLICATION = 'yogasite.wsgi.application'



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)




ADMINS = [('RegalAbode', 'regalabode@gmail.com'), ]

DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    

]






LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticcollection')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_URL = '/static/'
MEDIA_URL = '/static/img/'

VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

# TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR, 'media'),]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
HTML_EXT = ('html', 'htm')
HTML_CONTENT_TYPE = ('text/html',)
HTML_SIZE = 10 * 1024 * 1024
IMAGE_SIZE = 10 * 1024 * 1024



#SESSION_COOKIE_DOMAIN = ".automate.org"



FILE_UPLOAD_PERMISSIONS = 0o755
DATA_UPLOAD_MAX_NUMBER_FIELDS = None
LOGIN_URL = "/accounts/signin/"
TIME_PERIOD_IN_SECONDS = 90 * 24 * 60 * 60


# Logging settings


LOGFILE_SIZE = 10 * 1024 * 1024
LOGFILE_COUNT = 10
SITE_ID = 1
#LOG_BASE_DIRECTORY = '/var/log/automate/'

DURATION_DISCOUNT = {"1": 0, "2": 30, "3": 40}
'''LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s | %(levelname)s | %(module)s [%(process)d %(thread)d] | [%(filename)s:%(lineno)s - %(funcName)s() ] | \n%(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': LOGFILE_SIZE,
            'backupCount': LOGFILE_COUNT,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'smtp': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'contactlist_manager': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}'''


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'mailprocess.authentication.APIAuthentication',

    ]
}
