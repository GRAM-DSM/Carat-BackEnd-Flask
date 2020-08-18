from sqlalchemy import Column, String, ForeignKey, Integer

from Server.model import Base


class Caring(Base):

    __tablename__ = 'carings'

    id = Column(Integer, primary_key=True)
    user_email = Column(String(80), ForeignKey('users.email'))
    caring = Column(String(300))
    image = Column(String(400))
    carat_count = Column(Integer)
    recaring_count = Column(Integer)

    def __init__(self, email, caring, image, carat_count, recaring_count):
        self.user_email = email
        self.caring = caring
        self.image = image
        self.carat_count = carat_count
        self.recaring_count = recaring_count
