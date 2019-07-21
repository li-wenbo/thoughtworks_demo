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

from flask import current_app

from app import create_app, init_filehandler_logger, DEFAULT_ENV

env = os.environ.get('ENVIRON', DEFAULT_ENV).lower()

app = create_app(env)
init_filehandler_logger(app, logging.DEBUG)


@app.route('/')
def index():
    return 'hello world from {}!'.format(current_app.env)


class StateApp(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)


app.wsgi_app = StateApp(app.wsgi_app)

if __name__ == '__main__':
    app.run(debug=True)
