from sqlalchemy import Column, String, ForeignKey, Integer

from Server.model import Base


class FollowList(Base):

    __tablename__ = 'follow_list'

    follow_user_email = Column(String(80), ForeignKey('users.email'), primary_key=True)
    followed_user_email = Column(String(80), ForeignKey('users.email'), primary_key=True)

    def __init__(self, follow_email, followed_email):
        self.follow_user_email = follow_email
        self.followed_user_email = followed_email
