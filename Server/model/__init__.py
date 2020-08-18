from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# from Server import DATABASE_URL

engine = create_engine("mysql+mysqldb://root:heunyam@localhost:3306/carat?charset=utf8")
Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()


