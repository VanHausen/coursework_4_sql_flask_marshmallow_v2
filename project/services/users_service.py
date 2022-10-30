from sqlalchemy.orm import scoped_session

from project.dao import UserDAO
from project.exceptions import ItemNotFound
from project.schemas import user
from project.schemas.user import UserSchema
from project.services.base import BaseService
from project.tools.security import generate_password_digest, get_password_hash


class UsersService(BaseService):
    def __init__(self, session: scoped_session):
        super().__init__(session)
        self.dao = None

    def get_item_by_id(self, pk: int):
        user = UserDAO(self._db_session).get_by_id(pk)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def get_item_by_email(self, email):
        user = UserDAO(self._db_session).get_by_email(email)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def get_all_users(self):
        users = UserDAO(self._db_session).get_all()
        return UserSchema(many=True).dump(users)

    def create(self, user_d):
        user_password = user_d.get("password")
        if user_password:
            user_d["password"] = generate_password_digest(user_password)
        user = UserDAO(self._db_session).create(user_d)
        return UserSchema().dump(user)

    def update(self, new_pd):
        user = UserDAO(self._db_session).update(new_pd)
        return UserSchema().dump(user)


    def update_password(self, new_pd):
        user_password_1 = new_pd.get("password_1")
        user_password_2 = new_pd.get("password_2")
        return UserSchema().dump(user)

    # def update_password(self, email, old_password, new_password):
    #     user = self.dao.UserDAO(self._db_session).get_by_email(email)
    #     password_hash = user.password
    #
    #     if get_password_hash(password_hash=password_hash, password=old_password):
    #         new_password_hash = get_password_hash(new_password)
    #         user.password = new_password_hash
    #         self.dao.UserDAO(self._db_session).update(user)
    #         return UserSchema().dump(user)
    #     else:
    #         return None
    #

        # if compose_passwords(password_hash=password_hash, password=old_password):
        #     new_password_hash = generate_password_hash(new_password)
        #     user.password = new_password_hash
        #     self.dao.update(user)
        #     return self.dao
        # else:
        #     return None