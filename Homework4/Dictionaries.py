# dict 2 listisgan
keys: list = ['Ten', 'Twenty', 'Thirt']
values: list = [10, 20, 30]
numbers = dict(zip(keys, values))
print(numbers)

#შეაერთეთ ორი dict -ი
dict1 = {'Ten' : 10, 'Twenty' : 20, 'Thirty' : 30}
dict2 = {'Thirty' : 30, 'Forty' : 40, 'Fifty' : 50}
dict1.update(dict2)
print(dict1)

# ამოიღეთ dict -იდან 'history' -ს value

sampleDict = {
    "class":{
        "student":{
        "name": "Mike",
        "marks":{
            "physics":70,
            'history':80
        }
    }}
}
print(sampleDict["class"]["student"]["marks"]["history"])

"""შექმენით dictionary, 
რომელშიც შეინახავთ იუზერის მიერ შემოტანილ მონაცემებს მის შესახებ და შემდეგ დაბეჭდავთ კონსოლში. 
(ველების ვალიდაცია: სიყვები უნდა იყოს კაპიტალიზირებულ ფორმატში, 
 მაგ. nick თუ შემოიტანა იუზერმა თქვენ უნდა გადააკეთოთ Nick - ად)
"""

user_info = {}
username = input("enter your username: ")
age = int(input("Enter your age: "))
address = input('enter your address')

user_info['username'] = username.title()
user_info['age'] = age
user_info['address'] = address.title()

print(user_info)


"""შექმენით ლისტი, რომელშიც შეინახავთ ქალაქების მონაცემებს (dict -ი გამოიყენეთ).
 იპოვეთ ამ ქალაქებს შორის, ყველაზე მცირე და ყველაზე ბევრი მაცხოვრებელი რომელ ქალაქებს ყავს და დაწერეთ მათი სახელები კონსოლში 
 (თუ რამდენიმეა მაშინ ისინიც დაწერეთ)"""


cities = [
    {'Name': "City1",
     'population': 1793230},
     {'Name': "City2",
      "population": 1793340},
      {'Name': "City3",
       "population": 2503},
       {'Name': "City4",
        "population": 1},
        {'Name': "City5",
         "population": 1}
]

highest_population = cities[0]

for city in cities[1:]:
    if city['population'] > highest_population['population']:
        highest_population = city

print(highest_population)


"""მოცემულია ლისტი, სადაც წერია თანამშრომლების სახელები, ასევე მოცემულია default dict-ი სადაც წერია "default" მნიშვნელობები.
 თქვენი დავალებაა შექმნათ ამ თანამშრომლებისთვის ახალი ლისტი,
   რომელშიც შეინახავთ თანამშრომლის სახელს და + "მიადგამთ" default მნიშვნელობებს."""

employees = ["Kelly", "Emma", "John"]
defaults = {"designation": "Application Developer", "Salary": 8000}





"""მოცემულია ლისტი, სადაც წერია რა გასაღებები (key) უნდა ამოიშალოს employee dict-იდან.
 ამოშალეთ და დაპრინტეთ დარჩენილი მნიშვნელობები და გასაღებები.
*
10 points
"""

employee = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
#keys_to_remove = ["Name", "salary"]


