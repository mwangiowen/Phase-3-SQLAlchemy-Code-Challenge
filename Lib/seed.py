from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Restaurant, Customer, Review


engine = create_engine('sqlite:///restaurant.db')


Base.metadata.bind = engine


Session = sessionmaker(bind=engine)
session = Session()


restaurants = [
    Restaurant(name='Restaurant A', price=3),
    Restaurant(name='Restaurant B', price=4)
]

customers = [
    Customer(first_name='John', last_name='Doe'),
    Customer(first_name='Jane', last_name='Smith'),
    Customer(first_name='Bob', last_name='Johnson'),
    Customer(first_name='Alice', last_name='Williams'),
    Customer(first_name='Charlie', last_name='Brown'),
    Customer(first_name='Eva', last_name='Taylor'),
    Customer(first_name='David', last_name='Lee'),
    Customer(first_name='Grace', last_name='Moore'),
    Customer(first_name='Frank', last_name='White'),
    Customer(first_name='Helen', last_name='Clark')
]

reviews = [
    Review(star_rating=5, restaurant=restaurants[0], customer=customers[0]),
    Review(star_rating=4, restaurant=restaurants[1], customer=customers[1]),
    
]


session.add_all(restaurants + customers + reviews)


session.commit()


session.close()
