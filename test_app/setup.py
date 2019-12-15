from os import path

from dominate import tags

from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_bootstrap.forms import WTFormsRenderer
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy

from markupsafe import Markup


BASE_DIR = path.dirname(__file__)
DB_NAME = 'database.db'
DATABASE_PATH = path.join(BASE_DIR, DB_NAME)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_PATH}'
app.config['SECRET_KEY'] = 'powerful secretkey'
app.config['WTF_CSRF_SECRET_KEY'] = 'a csrf secret key'
# app.config['SQLALCHEMY_ECHO'] = True

Bootstrap(app)
db = SQLAlchemy(app)
nav = Nav()
nav.init_app(app)
admin = Admin(app)


class CorrectWTFormsRenderer(WTFormsRenderer):
    def _wrapped_input(
            self, node, type='text', classes=['form-control'], **kwargs,
    ):
        wrap = self._get_wrap(node)
        wrap.add(tags.label(node.label.text, _for=node.id))
        wrap.add(tags.input(type=type, _class=' '.join(classes), name=node.name, **kwargs))
        return wrap


@app.template_filter('render_form')
def render_form(form, **kwargs):
    r = CorrectWTFormsRenderer(**kwargs)
    return Markup(r.visit(form))
