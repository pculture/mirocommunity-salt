DEBUG = {% if pillar['settings']['debug'] %}True{% else %}False{% endif %}
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = "{{ pillar['settings']['secret_key'] }}"

ADMINS = (
    {% if pillar['settings']['error_email'] %}
        ('Admin', "{{ pillar['settings']['error_email'] }}")
    {% endif %}
)

MANAGERS = ADMINS

TIME_ZONE = '{{ pillar["settings"]["time_zone"] }}'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True
MEDIA_URL = '/media/'

DEFAULT_FROM_EMAIL = SERVER_EMAIL = "{{ pillar['settings']['server_email'] }}"
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Resource URLs
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Resource directories
MEDIA_ROOT = "{{ pillar['files']['media_dir'] }}"
STATIC_ROOT = "{{ pillar['files']['static_dir'] }}"

FACEBOOK_APP_ID = "{{ pillar['settings']['apis']['facebook']['app_id'] }}"
FACEBOOK_API_SECRET = "{{ pillar['settings']['apis']['facebook']['api_secret'] }}"

TWITTER_CONSUMER_KEY = "{{ pillar['settings']['apis']['twitter']['consumer_key'] }}"
TWITTER_CONSUMER_SECRET = "{{ pillar['settings']['apis']['twitter']['consumer_secret'] }}"

RECAPTCHA_PUBLIC_KEY = "{{ pillar['settings']['apis']['recaptcha']['public_key'] }}"
RECAPTCHA_PRIVATE_KEY = "{{ pillar['settings']['apis']['recaptcha']['private_key'] }}"

VIMEO_API_KEY = "{{ pillar['settings']['apis']['vimeo']['api_key'] }}"
VIMEO_API_SECRET = "{{ pillar['settings']['apis']['vimeo']['api_secret'] }}"

USTREAM_API_KEY = "{{ pillar['settings']['apis']['ustream']['api_key'] }}"

YOUTUBE_API_KEY = "{{ pillar['settings']['apis']['youtube']['api_key'] }}"

# Not exactly a "connection", but it needs to be isolated to production projects.
GOOGLE_ANALYTICS_UA = "{{ pillar['settings']['apis']['google_analytics']['ua'] }}"
GOOGLE_ANALYTICS_DOMAIN = "{{ pillar['settings']['apis']['google_analytics']['domain'] }}"

DATABASES = {
    'default': {
        'ENGINE': '{{ pillar["settings"]["db"]["engine"] }}',
        'NAME': '{{ pillar["settings"]["db"]["name"] }}',
        'USER': '{{ pillar["settings"]["db"]["user"] }}',
        'PASSWORD': '{{ pillar["settings"]["db"]["password"] }}',
        'HOST': '{{ pillar["settings"]["db"]["host"] }}',
        'PORT': '{{ pillar["settings"]["db"]["port"] }}',
        {% if pillar["settings"]["db"]["engine"] == 'django.db.backends.mysql' %}
        'OPTIONS': {'init_command': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED'},
        {% endif %}
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': '{{ pillar["settings"]["haystack"]["engine"] }}',
        'URL': '{{ pillar["settings"]["haystack"]["url"] }}',
        'INDEX_NAME': '{{ pillar["settings"]["haystack"]["index_name"] }}',
    }
}

CACHES = {
    'default': {
        'BACKEND': '{{ pillar["settings"]["cache"]["backend"] }}',
        'LOCATION': '{{ pillar["settings"]["cache"]["location"] }}',
    }
}


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_LOADERS = (
    'uploadtemplate.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware'
    'localtv.middleware.FixAJAXMiddleware',
    'localtv.middleware.UserIsAdminMiddleware',
    'openid_consumer.middleware.OpenIDMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

ROOT_URLCONF = 'localtv.urls'
WSGI_APPLICATION = "webproject.wsgi.application"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'djpagetabs',
    'localtv',
    'localtv.admin',
    'localtv.comments',
    'localtv.submit_video',
    'localtv.inline_edit',
    'localtv.user_profile',
    'localtv.playlists',
    'djvideo',
    'registration',
    'tagging',
    'haystack',
    'email_share',
    'djcelery',
    'notification',
    'socialauth',
    'openid_consumer',
    'daguerre',
    'compressor',
    'mptt',
    'uploadtemplate',
    'social_auth',
    'djcelery',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    "localtv.context_processors.localtv",
    "localtv.context_processors.browse_modules",
    "mirocommunity_saas.context_processors.tier_info",
)
AUTH_PROFILE_MODULE = 'user_profile.Profile'

UPLOADTEMPLATE_MEDIA_ROOT = MEDIA_ROOT + "uploadtemplate/"
UPLOADTEMPLATE_MEDIA_URL = MEDIA_URL + "uploadtemplate/"
# These settings seem to relate to how uploadtemplate fleshes out incomplete themes.
UPLOADTEMPLATE_STATIC_ROOTS = []
UPLOADTEMPLATE_TEMPLATE_ROOTS = []

# Localtv settings
# This is here for backwards-compat only.
COMMENTS_APP = 'localtv.comments'


# Compressor settings
COMPRESS_STORAGE = 'mirocommunity_saas.storages.CompressedBotoStorage'
COMPRESS_ENABLED = False


# Auth settings
# After people login, redirect them to root.
LOGIN_REDIRECT_URL = '/'
AUTH_PROFILE_MODULE = 'user_profile.Profile'
AUTHENTICATION_BACKENDS = (
    'localtv.auth_backends.MirocommunityBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.google.GoogleBackend',
)


SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    #'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)


# django-tagging settings
FORCE_LOWERCASE_TAGS = True


# django-registration settings
ACCOUNT_ACTIVATION_DAYS = 7


# Forward-compatibility for uploadtemplate changes.
UPLOADTEMPLATE_PROTECTED_TEMPLATE_NAMES = (
    r'^localtv/admin/',
    r'^uploadtemplate/',
    r'^goodies/',
    # Playlist templates are all admin templates.
    r'^playlists/',
    r'^comments/(moderation_queue|spam|spammed|*\.txt)',
)

UPLOADTEMPLATE_PROTECTED_STATIC_FILES = (
    r'admin',
)

import djcelery
djcelery.setup_loader()
BROKER_URL = 'amqp://localtv:localtv@localhost:5672/localtv'
CELERY_BACKEND = 'cache'
CELERY_SEND_TASK_ERROR_EMAILS = False
from kombu import Exchange, Queue
CELERY_DEFAULT_QUEUE = 'default_1_10'
CELERY_QUEUES = (
    Queue(CELERY_DEFAULT_QUEUE, Exchange(CELERY_DEFAULT_QUEUE), routing_key=CELERY_DEFAULT_QUEUE),
)
CELERY_ROUTES = {
    'localtv.tasks.haystack_update': {'queue': 'haystack_1_10'},
    'localtv.tasks.haystack_remove': {'queue': 'haystack_1_10'},
    'localtv.tasks.haystack_batch_update': {'queue': 'haystack_1_10'},
}

# Should let us use the normal logging set up in LOGGING for celery as well.
CELERYD_HIJACK_ROOT_LOGGER = False

# Kill workers if they're hung on a task for 5 minutes.
CELERYD_TASK_TIME_LIMIT = 300


