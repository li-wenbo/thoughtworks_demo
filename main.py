#! *-* utf-8 *-*
from app import create_app, init_logger
from flask import render_template
import requests

app = create_app(__name__)
init_logger(app)


@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True)

