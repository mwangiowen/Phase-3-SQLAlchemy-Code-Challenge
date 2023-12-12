from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Restaurant, Customer, Review


engine = create_engine('sqlite:///restaurant.db')


Base.metadata.bind = engine


Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)


session.commit()
session.close()
