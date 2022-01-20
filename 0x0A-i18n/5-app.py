#!/usr/bin/env python3
"""Setup Babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from os import getenv

app = Flask(__name__)
babel = Babel(app)
"""init Babel obj"""
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """get locale"""
    lang = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if lang in supportLang:
        return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """returns user dict"""
    try:
        userId = request.args.get('login_as')
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request():
    """find a user if exists"""
    g.user = get_user(request.args.get('login_as'))


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
