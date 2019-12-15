"""Example admin view:
admin.add_view(ModelView(Item, db.session))
"""

from flask_admin.contrib.sqla import ModelView

from .setup import admin, db
from .models import *
