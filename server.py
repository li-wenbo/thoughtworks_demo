#! *-* utf-8 *-*
"""
    server.py
    ~~~~~~~~~

    the wsgi call object, the entry to web app

    :copyright:
    :license:
"""
import logging
import os

from app import create_app, init_filehandler_logger, DEFAULT_ENV

env = os.environ.get('ENV', DEFAULT_ENV)

app = create_app(env)
init_filehandler_logger(app, logging.DEBUG)


@app.route('/')
def index():
    return 'hello world from {}!'.format(env)


if __name__ == '__main__':
    app.run(debug=True)
