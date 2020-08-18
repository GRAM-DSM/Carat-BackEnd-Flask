from sqlalchemy import Column, String, ForeignKey, Integer

from Server.model import Base


class Recaring(Base):

    __tablename__ = 'recarings'

    user_email = Column(String(80), ForeignKey('users.email'))
    caring_id = Column(Integer, ForeignKey('carings.id'))

    def __init__(self, email, caring_id):
        self.user_email = email
        self.caring_id = caring_id
