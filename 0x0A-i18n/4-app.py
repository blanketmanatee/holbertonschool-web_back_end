#!/usr/bin/env python3
"""Setup Babel"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from os import getenv

app = Flask(__name__)
babel = Babel(app)
"""init Babel obj"""


class Config(object):
    """Class Config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
"""config for flask"""


@app.route('/')
def route():
    """flask app"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """get locale"""
    lang = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if lang in supportLang:
        return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
