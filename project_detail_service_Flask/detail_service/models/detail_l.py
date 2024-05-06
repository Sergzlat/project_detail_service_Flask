from enum import Enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
# project_detail_service/detail_service/models/detail_l.py

from .database import Base


Base = declarative_base()

class UserType(Enum):
    Unknown = 0
    Nextdetail = 1
    DetailL = 2
    Admin = 3

class Entity:
    def __init__(self):
        self.id = None
        self.is_deleted = False

class DetailL(Base):
    __tablename__ = 'detail_ls'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    email = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)

    def __init__(self, first_name, middle_name, last_name, birth_date, email):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.is_deleted = False