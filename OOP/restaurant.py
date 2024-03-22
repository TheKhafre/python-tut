class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name} "
            f"\nWe are serving {self.cuisine_type} today")
        
    
    def open_restaurant(self):
        print("the restaurant is open! You can come in now.")
    

my_shop = Restaurant("Fancy foods", "spaghetti")
my_shop.describe_restaurant()

print(f"\n{my_shop.restaurant_name}")