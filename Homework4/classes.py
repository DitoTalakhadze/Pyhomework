#9.1
class Resturant:
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


