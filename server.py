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

env = os.environ.get('ENVIRON', DEFAULT_ENV).lower()

app = create_app(env)
init_filehandler_logger(app, logging.DEBUG)


@app.route('/')
def index():
    state = DEFAULT_ENV

    if not app.config['DEBUG'] and not app.config['TESTING']:
        state = 'production'

    if app.config['DEBUG']:
        state = 'dev'

    if app.config['TESTING']:
        state = 'test'

    return 'hello world from {}!'.format(state)


if __name__ == '__main__':
    app.run(debug=True)
