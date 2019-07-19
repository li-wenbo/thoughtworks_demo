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

config_map = {
    'production': config.ProductionConfig,
    'dev': config.DevelopmentConfig,
    'test': config.TestingConfig,
}

DEFAULT_ENV = 'dev'


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config_map.get(env, config.DevelopmentConfig))
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
