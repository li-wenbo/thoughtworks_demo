#! *-* utf-8 *-*
"""
    __init__.py
    ~~~~~~~~~

    app factory the helpers

    :copyright:
    :license:
"""


import logging

from flask import Flask

from . import config


# match the git branch
PRODUCTION_BRANCH_NAME = 'master'
DEV_BRANCH_NAME = 'dev'
TEST_BRANCH_NAME = 'testing'


config_map = {
    PRODUCTION_BRANCH_NAME: config.ProductionConfig,
    DEV_BRANCH_NAME: config.DevelopmentConfig,
    TEST_BRANCH_NAME: config.TestingConfig,
}

DEFAULT_ENV = TEST_BRANCH_NAME


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config_map.get(env, config.DevelopmentConfig))

    state = DEFAULT_ENV
    if not app.config['DEBUG'] and not app.config['TESTING']:
        state = PRODUCTION_BRANCH_NAME

    if app.config['DEBUG']:
        state = DEV_BRANCH_NAME

    if app.config['TESTING']:
        state = TEST_BRANCH_NAME

    app.env = state
    return app


def init_filehandler_logger(app, log_level, filename='flask.log'):
    """
    http://flask.pocoo.org/docs/1.0/logging/#basic-configuration will overwrite gunicorn logging config
    cause logging.getLogger is a Singleton method， so we can set the attr before flask.logging.create_logger
    :param app:
    :return:
    """

    import os.path
    log_filename = os.path.join(app.root_path, app.config['LOGDIR'], filename)

    logger = logging.getLogger(app.name)
    logger.setLevel(log_level)
    fh = logging.FileHandler(log_filename)
    fh.setLevel(log_level)
    fh.setFormatter(logging.Formatter('%(asctime)s|%(process)d - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(fh)
