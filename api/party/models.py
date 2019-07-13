import datetime
from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, Party_Status


class Party(Base, Utility):
    __tablename__ = 'parties'
    id = Column(Integer, Sequence('parties_id_seq', start=1), primary_key=True)  # noqa
    party_name = Column(String, unique=True, nullable=False)
    hq_address = Column(String, nullable=False)
    logo_url = Column(String, nullable=True)
    status = Column(Enum(Party_Status), default="new")
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)
