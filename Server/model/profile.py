from sqlalchemy import Column, String, ForeignKey

from Server.model import Base


class Profile(Base):

    __tablename__ = 'profiles'

    user_email = Column(String(80), ForeignKey("users.email", name="profiles_user_email_fkey"), primary_key=True)
    name = Column(String(80))
    profile_image = Column(String(120))
    cover_image = Column(String(120))
    about_me = Column(String(100))


    def __init__(self, user_email, name, profile_image, cover_image, about_me):
        self.user_email = user_email
        self.name = name
        self.profile_image = profile_image
        self.cover_image = cover_image
        self.about_me = about_me
