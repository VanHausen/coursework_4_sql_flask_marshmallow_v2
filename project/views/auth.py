from flask_restx import abort, Namespace, Resource
from flask import request
from requests import api

from project.dao import user
from project.services import users_service
from project.tools.security import login_user, refresh_user_token
from project.exceptions import ItemNotFound
from project.services.users_service import UsersService
from project.setup_db import db

auth_ns = Namespace('auth')
secret = 's3cR$eT'
algo = 'HS256'


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in [email, password]:
            abort(400)
        try:
            user = UsersService(db.session).get_item_by_email(email=email)
            tokens = login_user(request.json, user)
            return tokens, 201
        except ItemNotFound:
            abort(401, "ошибка авторизации")

    def put(self):
        req_json = request.json
        if None in req_json:
            abort(400)

        try:
            tokens = refresh_user_token(req_json)
            return tokens, 200
        except ItemNotFound:
            abort(401, "ошибка авторизации")

@auth_ns.route('/register')
class AuthRegView(Resource):
    def post(self):
        req_json = request.json
        if None in req_json:
            abort(400, "не корректный запрос")
        return UsersService(db.session).create(req_json)

# @api.route('/register/')
# class RegisterView(Resource):
#     @api.marshal_with(user, as_list=True, code=200, description='OK')
#     def post(self):
#         data = request.json
#         if data.get('email') and data.get('password'):
#             return users_service.create(data.get('email'), data.get('password')), 201
#         else:
#             return "Чего-то не хватает", 401
#     @api.response
#     def put(self):
#         data = request.json
#         if data.get('access_token') and data.get('refresh_token'):
#             return users_service.update(data.get('access_token'), data.get('refresh_token')), 201
#         else:
#             return "Чего-то не хватает", 401

