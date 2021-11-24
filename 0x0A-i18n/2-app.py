#!/usr/bin/env python3
"""Setup Babel"""
from flask import Flask, render_template
from flask_babel import Babel

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
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.confit['LANGUAGES'])


if __name__=="__main__":
    app.run()