import os
import datetime
import bcrypt
import jwt

from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.schema import Sequence
from sqlalchemy.event import listen

from helpers.database import Base
from utilities.utility import Utility, UserType

secret = os.getenv('SECRET_KEY')


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq', start=1), primary_key=True) # noqa
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    other_names = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    user_type = Column(Enum(UserType), default="citizen")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)

    @staticmethod
    def pre_save(mapper, connect, target):
        target.hash_password()

    def hash_password(self):
        hashed_password = bcrypt.hashpw(
            self.password.encode('utf-8'),
            bcrypt.gensalt()
        )

        self.password = hashed_password.decode('utf-8')

        return self.password

    def generate_token(self):
        token = jwt.encode(
            {'id': str(self.id), 'user_type': self.user_type.value},
            secret,
            algorithm='HS256'
        )

        return token.decode('utf-8')

    @staticmethod
    def decode_token(token):
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256']
        )

        return payload


listen(User, 'before_insert', User.pre_save)
