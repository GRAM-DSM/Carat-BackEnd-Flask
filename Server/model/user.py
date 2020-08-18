from datetime import datetime
from sqlalchemy import Column, String

from Server.model import Base


class User(Base):

    __tablename__ = 'users'

    email = Column(String(80), primary_key=True)
    hashed_password = Column(String(120))

    def __init__(self, email, password):
        self.email = email
        self.hashed_password = password
