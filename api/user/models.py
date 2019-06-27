from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, UserType


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq', start=1, increment=1), primary_key=True) # noqa
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    other_names = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    user_type = Column(Enum(UserType), default="admin")
