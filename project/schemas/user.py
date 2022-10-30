from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int(required=True, example=1)
    email = fields.Str(required=True, example='fields@gmail.com')
    password = fields.Str(required=True, example='1f2344vvcv')
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()