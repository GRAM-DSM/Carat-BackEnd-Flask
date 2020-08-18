from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import SQLAlchemyError

from Server.model import session
from Server.model.user import User
from Server.model.profile import Profile


def create_new_user(name, email, password):
    new_user = User(email=email, password=generate_password_hash(password))
    new_profile = Profile(user_email=email,
                          name=name,
                          profile_image="default_profile.png",
                          cover_image="default_cover.jpg",
                          about_me="...")

    session.add(new_user)
    session.commit()
    session.add(new_profile)
    session.commit()


def sign_up(name, email, password):

    user = session.query(User).filter(User.email == email).first()

    if user:
        return abort(409, "This email is already sign up")

    try:

        create_new_user(name, email, password)

        return {
            "message": "Successfully signed up"
        }

    except SQLAlchemyError:
        session.rollback()
        return abort(500, "db_error")


def login(email, password):

    try:
        user = session.query(User).filter(User.email == email).first()
        check_user_password = check_password_hash(user.password, password) if user else None

        if check_user_password:

            access_token = create_access_token(identity=email)

            return {
                "access_token": access_token
            }

        else:
            return abort(400, "The email or password is incorrect")

    except SQLAlchemyError:
        session.rollback()
        return abort(500, "db_error")



