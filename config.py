import os

basedir = os.path.abspath(os.path.dirname(__file__))


def get_postgresql_url():
    return 'postgres://postgres:postgres@{host}:{port}/antiques'.format(
        host=os.environ.get('POSTGRES_HOST', 'localhost'),
        port=5432,
    )


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''
    ASSETS_DEBUG = False
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_postgresql_url()
    SECRET_KEY = 'very-secret-key'
    HOST_URL = 'http://antiques.vgamula.me'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_postgresql_url()
    DEBUG = True
    SECRET_KEY = 'not-secret'
    ASSETS_DEBUG = True
    HOST_URL = 'http://antiques.dev:5000'
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    PROFILER_ENABLED = True
    PROFILER_VERBOSE = False
