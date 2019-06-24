import enum
import api
from helpers.database import db_session
from sqlalchemy import event

class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()


class UserType(enum.Enum):
    admin = "admin"
    politician = "politician"
    citizen = "citizen"
