#!/usr/bin/env python3
"""Basic Flask"""

app = Flask(__name__)


@app.route('/')
def root():
    """Basic Flask App"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()