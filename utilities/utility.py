from enum import Enum
from helpers.database import db_session


class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()


class UserType(Enum):
    admin = "admin"
    politician = "politician"
    citizen = "citizen"


class Party_Status(Enum):
    new = "new"
    updated = "updated"


class Office_Status(Enum):
    new = "new"
    updated = "updated"


class OfficeType(Enum):
    federal = "federal"
    legislative = "legislative"
    local_government = "local_government"
    state = "local-government"
