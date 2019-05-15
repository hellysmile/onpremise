import os

from elasticsearch import Elasticsearch
from sentry.conf.server import *  # noqa
from sentry.utils.types import Bool

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'sentry.db.postgres',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': os.environ['SENTRY_POSTGRES_HOST'],
        'PORT': '5432',
        'OPTIONS': {
            'autocommit': True,
        },
    },
}

es = Elasticsearch([os.environ['SENTRY_ELASTICSEARCH_HOST'] + ':9200'])
SENTRY_NODESTORE = 'sentry_elastic_nodestore.ElasticNodeStorage'
SENTRY_NODESTORE_OPTIONS = {
    'es': es,
}

SENTRY_USE_BIG_INTS = True

SENTRY_SINGLE_ORGANIZATION = True

SENTRY_OPTIONS.update({
    'redis.clusters': {
        'default': {
            'hosts': {
                0: {
                    'host': os.environ['SENTRY_REDIS_HOST'],
                    'password': '',
                    'port': '6379',
                    'db': '0',
                },
            },
        },
    },
})

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append('sentry_elastic_nodestore')
INSTALLED_APPS = tuple(INSTALLED_APPS)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://' + os.environ['SENTRY_REDIS_HOST'] + ':6379/1',
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
    },
}

SESSION_ENGINE = 'redis_sessions_fork.session'
SESSION_REDIS_URL = 'redis://' + os.environ['SENTRY_REDIS_HOST'] + ':6379/2'

SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

BROKER_URL = 'librabbitmq://guest:guest@' + os.environ['SENTRY_RABBITMQ_HOST'] + ':5672//'

# for queue in CELERY_QUEUES:
#     queue.durable = True

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

SENTRY_DIGESTS = 'sentry.digests.backends.redis.RedisBackend'

SENTRY_OPTIONS['filestore.backend'] = 'filesystem'
SENTRY_OPTIONS['filestore.options'] = {
    'location': None,
}

if Bool(os.environ['SENTRY_USE_SSL']):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'protocol': os.environ['SENTRY_WEB_PROTOCOL'],
    'workers': int(os.environ['SENTRY_WEB_WORKERS']),
}

# SENTRY_OPTIONS['mail.backend'] = 'smtp'
# SENTRY_OPTIONS['mail.host'] = os.environ['SENTRY_EMAIL_HOST']
# SENTRY_OPTIONS['mail.password'] = ''
# SENTRY_OPTIONS['mail.username'] = ''
# SENTRY_OPTIONS['mail.port'] = 25
# SENTRY_OPTIONS['mail.use-tls'] = False
# SENTRY_OPTIONS['mail.from'] = 'sentry@ocean.io'
SENTRY_OPTIONS['mail.backend'] = 'dummy'

SENTRY_OPTIONS['system.secret-key'] = os.environ['SENTRY_SECRET_KEY']
