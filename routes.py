# app/routes.py
from flask import render_template

def setup_routes(app):
    @app.route('/homePage')
    def homepage():
        return render_template('homepage.htm')

    @app.route('/')
    def login():
        return render_template('login.htm')
