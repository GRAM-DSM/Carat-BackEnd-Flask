from sqlalchemy import Column, String, ForeignKey, Integer

from Server.model import Base


class CaratList(Base):

    __tablename__ = 'carat_list'

    carat_user_email = Column(Integer, auto_increment=True, primary_key=True)
    caring_id = Column(String(80), ForeignKey('carings.id'))

    def __init__(self, email, caring_id):
        self.user_email = email
        self.caring_id = caring_id
