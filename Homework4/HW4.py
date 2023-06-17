# 6.1 

Person1 = {"first_name": "Kenny",
         "last_name": "McCormick",
         "age": 9,
         "city": "SP"}
print(Person1)
print(Person1['first_name'])
print(Person1['last_name'])
print(Person1['age'])
print(Person1['city'])

#6.2
fav_numbers = {"Bob": "blue",
               "Ahmad": "green",
               "jackie": "yellow"}
print(fav_numbers["Bob"])
print(fav_numbers["Ahmad"])
print(fav_numbers["jackie"])

#6.3
words = {"lists": "we can store data in lists",
         "slice": "we can slice lists",
         "sort": "we can sort elements"}
print(words)


#6.4 
words = {"lists": "we can store data in lists",
         "slice": "we can slice lists",
         "sort": "we can sort elements"}
for k, v in words.items():
    print(f"{k} >>> {v}")

#6.5

rivers = {"Mtkvari": "Georgia",
          "Amazon": "South America",
          "Po": "Italy"}
for name, country in rivers.items():
    print(F"{name} runs through {country}")

for name in rivers.keys():
    print(F"{name} is very beautiful")

for country in rivers.values():
    print(F"{country} has many other beautiful rivers")


#6.6

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
    
students = ["bob", "jen", "herbert", 'lester', 'phil']

for student in students:
    if student in favorite_languages:
        print(F"thank you {student} for responding")
    else:
        print(F"please {student} take a look at our poll")

#6.7

Person1 = {"first_name": "Kenny",
         "last_name": "McCormick",
         "age": 9,
         "city": "SP"}
person2 = {"first_name": "Bob",
         "last_name": "Bobson",
         "age": 196,
         "city": "Paradise"}
person3 = {"first_name": "Ben",
         "last_name": "Dover",
         "age": 90,
         "city": "Bikini Bottom"}
people = [Person1, person2, person3]

print(people)

for person in people:
    print(person)
    
#6.8
doctor_pain = {
    "type": "cat",
    "owner": "Dr.Doom"
}
slinger = {
    "type": "monkey",
    "owner": "John"
}
mr_kitty = {
    "type": "dog",
    "owner": "Ivy"
}
pets = []
pets.append(mr_kitty)
pets.append(slinger)
pets.append(doctor_pain)
print(pets)

for pet in pets:
    type = pet["type"]
    owner = pet["owner"]
    print(f"{pet} is a {owner}'s {type}")

#6.9
fav_places = {"jack": ["black pearl", "tavern", "jail"],
              "butters": ["home", "school"],
              "zavala": ["balcony"]}
for name, place in fav_places.items():
    if len(place) > 1:
        print(F"{name}'s favourite places are {place}")
    else:
        print(F"{name}'s favourite place is {place}")




