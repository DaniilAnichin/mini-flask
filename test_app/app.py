"""Example view:
@app.route('/tests/')
def tests():
    test_item = Item.query.filter_by(item_type='test').first()
    return render_template('item.html',  item=test_item)
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_nav.elements import Navbar, View

from .admin_views import admin
from .forms import *
from .setup import app, db, nav
from .models import *


test_app = Blueprint('test_app', __name__)


nav.register_element(
    'frontend_top',
    Navbar(
        View('TestApp', '.index'),
    )
)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Run with: FLASK_DEBUG=1 FLASK_APP=test_app.app flask run
    app.run()
