# bookpage = 497
# username= shopadmin
# password = testing321
import mimetypes
import os

from braintree import Configuration, Environment

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 't(z&7lq9b*l9-qj#0u)4m0ekys2w(l!xh1h!=!kztopx&xyutr'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # local apps
    'coupons.apps.CouponsConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'cart.apps.CartConfig',
    'shop.apps.ShopConfig',
    # ...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware'  # <======
    # must be after session and before common middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'cart.context_processors.cart',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGE = (
    ('en', 'English'),
    ('es', 'Spanish'),
)

TIME_ZONE = 'Asia/karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'  # this is our local path where our media located
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CART_SESSION_ID = 'cart'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

BRAINTREE_MERCHANT_ID = os.environ.get('Merchant ID')
BRAINTREE_PUBLIC_KEY = os.environ.get('Public Key')
BRAINTREE_PRIVATE_KEY = os.environ.get('Private Key')

Configuration.configure(Environment.Sandbox,
                        merchant_id=BRAINTREE_MERCHANT_ID,
                        private_key=BRAINTREE_PRIVATE_KEY,
                        public_key=BRAINTREE_PUBLIC_KEY)

# mimetypes.add_type("text/css", ".css", True)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
