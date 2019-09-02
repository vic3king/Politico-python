import datetime
from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey)
from sqlalchemy import UniqueConstraint
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, Office_Status, OfficeType


class Candidate(Base, Utility):
    __tablename__ = 'candidates'
    id = Column(Integer, Sequence('candidates_id_seq', start=1), primary_key=True)  # noqa
    office_id = Column(Integer, ForeignKey('offices.id', ondelete="CASCADE"))
    party_id = Column(Integer, ForeignKey('parties.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    status = Column(Boolean, nullable=False, default=False)
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
    UniqueConstraint('user_id')
    
