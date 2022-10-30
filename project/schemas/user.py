from marshmallow import fields, Schema

from load_fixtures import genre


class UserSchema(Schema):
    id = fields.Int(required=True, example=1)
    email = fields.Str(required=True, example='fields@gmail.com')
    password = fields.Str(required=True, max_length=100,  example='1f2344vvcv')
    name = fields.Str(required=True, max_length=100,  example='Evgen')
    surname = fields.Str(required=True, max_length=100, example='Komarov')
    favorite_genre = fields.Str(required=True, max_length=100)