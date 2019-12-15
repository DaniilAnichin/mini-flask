"""Example form:

class TestForm(Form):
    answers = fields.RadioField(label='Answer: ')
    confirm = fields.SubmitField(label='Save')
"""
from random import shuffle

from flask_wtf import Form, form
from wtforms import fields, widgets


__all__ = (
)
