import base64
import hashlib

from project.dao.models.base import BaseMixin
from project.setup_db import db

class User(BaseMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String)

    def __repr__(self):
        return f"<User '{self.name.title()}'>"






    # def get_password(password):
    #     return hashlib.md5(password.encode('utf-8')).hexdigest()
    #
    # def get_password_hash(password):
    #     return base64.b64encode(password.get_password(password)).decode('utf-8')