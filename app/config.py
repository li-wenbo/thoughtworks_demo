#! *-* utf-8 *-*
"""
    config.py
    ~~~~~~~~~

    prod config, dev config, test config

    :copyright:
    :license:
"""


class Config(object):
    DEBUG = False
    TESTING = False
    LOGDIR = 'logs'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
