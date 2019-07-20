import datetime
from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, Office_Status, OfficeType


class Office(Base, Utility):
    __tablename__ = 'offices'
    id = Column(Integer, Sequence('offices_id_seq', start=1), primary_key=True)  # noqa
    office_name = Column(String, unique=True, nullable=False)
    age_limit = Column(String, nullable=False)
    office_type = Column(Enum(OfficeType), default="local_government")
    description = Column(String, nullable=False)
    status = Column(Enum(Office_Status), default="new")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
