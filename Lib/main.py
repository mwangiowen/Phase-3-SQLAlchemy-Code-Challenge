
from database import Session
from Migration import Base, engine, Restaurant, Customer, Review

def main():
    
    Base.metadata.create_all(engine)

   
    session = Session()

    try:
        
        restaurant1 = Restaurant(name='Restaurant A', price=3)
        restaurant2 = Restaurant(name='Restaurant B', price=4)
        customer1 = Customer(first_name='Owen', last_name='Smith')
        customer2 = Customer(first_name='Kevin', last_name='Lawrence')
        review1 = Review(star_rating=5, restaurant=restaurant1, customer=customer1)
        review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

        
        session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

       
        session.commit()

       
        restaurants = session.query(Restaurant).all()
        for restaurant in restaurants:
            print(f"Restaurant: {restaurant.name}, Price: {restaurant.price}")

    finally:
       
        session.close()

if __name__ == "__main__":
    main()