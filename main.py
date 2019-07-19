#! *-* utf-8 *-*
from app import create_app, init_logger
from flask import render_template, request
import requests

app = create_app(__name__)
init_logger(app)


@app.route('/')
def index():
    return 'hello world! {}'.format(app.config.get('ENV', ''))


if __name__ == '__main__':
    app.run(debug=True)

