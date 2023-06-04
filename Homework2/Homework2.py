"""Homework N2 """

print("Greetings")

"""exercise 5.1 """

#conditional tests with my predictions

tank = "panther"
print("is tank == 'panther'? my preditcion is true")
print(tank == "panther")
tank = "tiger"
print("my prediction tiger - true")
print(tank == "tiger")
car = 'fiat'
print("my prediction fiat - true")
print(car == "fiat")
print("tank == 'fiat' my prediction is false")
print(tank == "fiat")
print("car =='panther' my prediction - false")
print(car == "panther")
"""exercise 5.2"""

#test for equality and inequality 

fruit = "orange"
if fruit == "orange":
    print("orange is a fruit")

order = "steak"
if order != "burger":
    print("sorry we only serve burgers")

#test with lower() - example: someone chose "Mazda" in filter/searach.

manufacturer = "Mazda"
if manufacturer.lower() == 'mazda':
    print("here are your search results for mazda")

#numerical tests - example age verification for the web

age = 25
if age >=18:
    print("thanks for confirming! you can browse this website")
else:
    print("sorry you are not eligible to visit this website")

#example - math I guess 

answer = 25
if answer == 94500:
    print("good job you are very smart!")
else:
    print("you are a dummy!")

# and, or keywords. 

age_1 = 20
age_2 = 30
if age_1 >= 6 or age_2 >=6:
    print("sorry your 'kids' are too old for a kindergarten")
else:
    print("your request will be reviwed by our administration, thanks!")
car = "subaru"
fast = 'subaru'
if car == "subaru" and fast == "subaru":
    print("you have a fast car")
else:
    print("either you have a slow car or dont have a card")

# test value in a list 

animals_in_the_zoo = ["bear", "gorrila", "lion", "otter", "cheetah"]
print("bear" in animals_in_the_zoo)

# test value not in a list

students = ['john', 'jack', 'mario', 'obama']
user = 'dito'
if user not in students:
    print(f"{user} is not a student")

"""excersies 5.3"""

#Alien colors 

alien_color = "green"
if 'green' in alien_color:
    print('you earned 5 points')
alien_color = "red"
if 'green' in alien_color:
    print('you earned 5 points')

#Alien colors 2 - runs else

alien_color = "yellow"
if "green" in alien_color:
    print("5 points")
else:
    print("you earned 10 points")

# runs if

alien_color = "green"
if "green" in alien_color:
    print("5 points")
else:
    print("you earned 10 points")

#Alien colors 3 
alien_color = "green"
if 'green' in alien_color:
    print("5 points")
elif 'yellow' in alien_color:
    print('10 points')
elif "red" in alien_color:
    print('15 points')

alien_color = "yellow"
if 'green' in alien_color:
    print("5 points")
elif 'yellow' in alien_color:
    print('10 points')
elif "red" in alien_color:
    print('15 points')

alien_color = "red"
if 'green' in alien_color:
    print("5 points")
elif 'yellow' in alien_color:
    print('10 points')
elif "red" in alien_color:
    print('15 points')

#stages of life

age = 25 
if age < 2:
    print("baby")
elif age >=2 and age < 4:
    print("toddler")
elif age >=4 and age < 13:
    print('kid')
elif age >= 13 and age < 20:
    print('teen')
elif age >=20 and age < 65:
    print('adult')
elif  age >= 65:
    print("elder")

# favourite fruits 

favourite_fruits = ["orange", "cherry", "apple"]
if "orange" in favourite_fruits:
    print("orange is the best")

if 'cherry' in favourite_fruits:
        print("cherry is the best")

if "apple" in favourite_fruits:
            print("apple is the best")
if 'watermelon' in favourite_fruits:
    print("")
else:
    print("I also like watermenlon but its not on the top of the list")
if 'peach' in favourite_fruits:
    print("")
else:
    print("I also like peach but its not on the top of the list")

"""5.8"""

#hello admin. 


