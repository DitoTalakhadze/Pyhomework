#9.1
"""class Resturant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_resturant(self):
        print(f"{self.name} has {self.cuisine} cuisine")
    
    def open_resturant(self):
        print(F"{self.name} is open now!")


my_resturant = Resturant("Maroooon", "Italian")

my_resturant.describe_resturant()

my_resturant.open_resturant()

print(F"my resturants name is {my_resturant.name}")

resturant2 = Resturant("Furious Snail", "French")
resturant3 = Resturant("Khachapuri Enjoyers United", "Georgian")

resturant2.describe_resturant(), resturant3.describe_resturant()

resturant3.open_resturant()

resturants = [my_resturant, resturant2, resturant3]

resturants[2].describe_resturant()
"""
#9.3 
class User:
    def __init__(self, first_name, last_name, age, email):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.email = email
    def describe_user(self):
        print(F'here is requested user info: {self.fname, self.lname, self.age, self.email} ')
    def greet_user(self):
        print(F"Hello user {self.fname} {self.lname} how are you")

user1 = User('Nick', 'Cage', 96, 'ncage@ncage.com')

user1.describe_user()
user1.greet_user()

#9.4 

class Resturant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    
    def describe_resturant(self):
        print(f"{self.name} has {self.cuisine} cuisine")
    
    def open_resturant(self):
        print(F"{self.name} is open now!")

    def check_number_served(self):
        print(f"resturant has served {self.number_served} customers")

    def update_number_served(self, customers):
        self.number_served = customers

    
    def increment_number_served(self, customers):
        self.number_served += customers


my_resturant = Resturant("Maroooon", "Italian")

my_resturant.describe_resturant()

my_resturant.open_resturant()

print(F"my resturants name is {my_resturant.name}")

resturant2 = Resturant("Furious Snail", "French")
resturant3 = Resturant("Khachapuri Enjoyers United", "Georgian")

resturant2.describe_resturant(), resturant3.describe_resturant()

resturant3.open_resturant()

resturants = [my_resturant, resturant2, resturant3]

resturants[2].describe_resturant()

resturant5 = Resturant("Viris shaurma", "Georgian")

resturant5.describe_resturant()
resturant5.open_resturant()

resturant5.check_number_served()
resturant5.update_number_served(5)
resturant5.check_number_served()
resturant5.increment_number_served(10)
resturant5.check_number_served()



