#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_babel import Babel, numbers, dates
from datetime import date, datetime


app = Flask(__name__)
app.config['BABEL_DEFAULT_CONFIG'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # lang = request.accept_languages.best_match(['en', ''])
    return 'en'

d = date(2024, 12, 23)
nums = {'us': numbers.format_decimal(1.234, locale='en_US'),
        'de': numbers.format_decimal(1.234, locale='de'),
        'se': numbers.format_decimal(1.234, locale='se')
        }
days = {
    'us': dates.format_date(d, locale='en_US'),
    'de': dates.format_date(d, locale='de'),
    'se': dates.format_date(d)
}

@app.route('/')
def show():
    return render_template('index.html', res=nums, dates=days)

if __name__ == '__main__':
    app.run(debug=True)