"""Example model:
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    next_item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True, unique=True)

    next_item = db.relationship(
        'Item',
        remote_side=[id],
        foreign_keys=[next_item_id],
        backref=db.backref('prev_item', uselist=False)
    )

    root = db.Column(db.Boolean(), default=False)
    item_type = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'Item #{self.id} ({self.item_type})'

    @property
    def content(self):
        return getattr(self, self.item_type, None)

setup models with:
    db.create_all()
    db.session.commit()
"""
from .setup import db


__all__ = (
)
