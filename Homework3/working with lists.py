"""რა არის list?
*
1 point
ლისტ არის ელემენტების ერთობლიობა, ელემეტები შეიძლება იყოს სახელები, ფასები, გვეხმარება უკეტ ორგაიზებაში და გვაძლევს საშვალებას მათზე გარკვეულ იოპერაციები შევასტულოთ
რა არის ელემენტი?
*
1 point
ელემენტები არის ლისტში შემავალი ინფორმაცია
როგორ ვწვდებით ლისტის ელემენტებს?
*
1 point
ლისტის ელემენტებს გააჩნია ინდექსები, ინდექსის დახმარებით შეგვიძლია მივწვდეთ ელემენტს. 
დაწერეთ კოდი, რომელიც მოცემულ ლისტში ყველა ელემენტს გადაიყვანს მაღალ რეგისტრში (Upper case)

usernames = ["Nick", "Theo", "Theodor", "Mary", "nana", "manana"]
*
1 point"""
usernames = ["Nick", "Theo", "Theodor", "Mary", "nana", "manana"]
for upper_usernames in usernames:
    print(upper_usernames.upper())


"""დაწერეთ კოდი, რომელიც შემნის 1000 ელემენტიან ლისტს, სადაც იქნება მხოლოდ მარტივი რიცხვები (Prime Numbers, რიცხვები, რომლებიც იყოფა მხოლოდ 1-ზე და თავის თავზე)
5 points



რას აკეთებს შემდეგი კოდი?
აღწერეთ თითეული ხაზი!
"""
products = [
    ['Google Pixel 7', 1000],
     ['Chevy Volt 2918', 15000],
     ['Macbook Pro M2', 3499],
     ['Microsoft Surface Pro 2', 3649]
] # მოცემული გვაქვს პროდუქტების სია და მათი ფასები. 

for i, product in enumerate(products):
    print(f'[{i}]] {product[0]} - {product[1]}') # ლუპში გავუშვით i - მივანიჭეთ ინდექსი და ამ ინდექსის შესაბამისი დასახელება და შემდეგ ფასი. f' ს გამოყენებით გავაკეთეთ სია ინდექსი, დასახელება და გვერდით ფასი

chosen_product = input("Choose product: ")  # იუსერისთვის დავაყენეთ ინფუთი და ამ ინფუთიტ დავაესაინეთ კლიენტის მიერ არჩეული პროდუქტი chosen_prduct -ს, იუსერი ირჩევს ინდექსის მეშვეობით. 

product_to_purchase = None    # ვამოწმებთ სწორად აირჩია თუ არა იუსერმა პროდუქტი, თუ None მივიგებთ ნიშნავს რომ არ არის სწორად არჩეული და ბოლოში მიიღებს შესაბამის ტექსტს 
if chosen_product.isdigit():  #  თუ დიჯიტი წერია 
    chosen_product = int(chosen_product)  #გადაყავს დიჯიტი ინტეგერში რათა სწორედ მოხდეს ინდექსის არჩევა. თუ ვერ შესრულდა ვუბრუნდებიტ None-s.
    if chosen_product <= len(product):  # თუ იუსერმა აირჩია len ზე მეტი, ანუ გასცდა მოცემული ინდექსების ფარგლებს ამით ისევ სრულდევა if ლოგიკა და სჰედეგად გვაძლევს none. 
        product_to_purchase = products[chosen_product] # იუსერის მიერ არჩეულმა ინფუთმა გადალახა if ით მოცემული პირობები ნიშჰნავს რომ არჩეული პროდუქტი დაესაინდება product_to_purchase 

if product_to_purchase is None: # თუ None მივიგებთ ნიშნავს რომ არ არის სწორად არჩეული და ბოლოში მიიღებს შესაბამის ტექსტს 
    print("Selected product does not exist")
else:
    print(F"You have Chosen {product_to_purchase[0]}, price: {product_to_purchase[1]} USD") # ინპუთში სწორად იყო ჩაწერილი, ანუ არჩეული პროდუქტი სიაშია, დააკმაყოფილა ნუმბერ, ინტეგერ, ინდექსის სიგრძესაც არ გახსნა შედეგად მიიღო პასუხი დასახელება + ფასი 


"""
10 points
Captionless Image
წინა დავალებაში მოცემული ლისტის გამოყენებით,
იპოვნეთ პროდუქტი სახელის მიხედვით
*
5 points"""

products = [
    ['Google Pixel 7', 1000],
     ['Chevy Volt 2918', 15000],
     ['Macbook Pro M2', 3499],
     ['Microsoft Surface Pro 2', 3649]
] 

for i, product in enumerate(products):
    print(f'[{i}]] {product[0]} - {product[1]}') 

search = input("Enter name: ")  

for product in products:
    if search.lower() in product[0].lower():
        print(F'result for {product[0]} - price {product[1]} USD')
        







"""
დაწერეთ კოდი, რომელშიც გექნებათ მომხმარებლების სია:

users = [
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"] 
]

მომხმარებელს ავტორიზაცია გაატარეთ (შემოატანინეთ username და password) თუ ვერ გაიარა ავტორიზაცია quit() ფუნქციით შეაჩერეთ პროგრამა
*
5 points"""

users = [
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"] 
]

username = input("Enter your username: ")
password = input("Enter your password: ")

authorized = False

for user in users:
    if user[0] == username and user[1] == password:
        authorized = True
        break

if authorized:
    print("Authorization successful!")
else:
    print("Authorization failed.")





"""
წინა დავალებებში დაწერილი კოდი (პროდუქტის არჩევაზე და მომხმარებლის ავტორიზაციაზე) გამოიყენეთ და მომხმარებელს პროდუქტი აარჩევინეთ მხოლოდ იმ შემთხვევაში თუ ავტორიზაცია გავლილი აქვს.
*
5 points

users = [
["Legend27", "a1s2d3f4"],
["james123", "c5bt43f4"],
["DaveIsGreat", "wlervtb3r"]
]

balances = [
150000,
12000,
19000
]
ბალანსი ჩაამატეთ შესაბამის ინექსზე users ლისტში (მაგ. განახლებულ ლისტში მეორე ინდექსე მდგომ ელემენტს ასეთი სახე უნდა ჰქონდეს ["james123", "c5bt43f4", 12000])
*

5 points
შეავსეთ ლისტი იმ ასოებით, რომლებიც აკლია პირველიდან ბოლო ელემენტამდე 

alphabet_part = ['c', 'h', 'e']

(ამ შემთხვევაში a-დან h-მდე უნდა შეივსოს მხოლოდ)
უკეთესი იქნება თუ კოდი სხვა ასოებზეც იმუშავებს
*
10 points

რა არის list slicing? (alphabet[:5])
აღწერეთ მისი მუშაობის პრინციპი
*
1 point
list slicing - საშვალებას გვაძლევს ლისტიდან ამოვიღოთ ლისტის ნაწილი, ფრაგმენტი და გავაკეთოდ ახალი ლისტი, შეგვიძლია მივითითოთ დასაწყისი, დასასრული რის მიხედვითაც მოგვცემს ახალ ლისტს. 
ამ შემთხვევაში მივიღებტ ალფაბეტის პირველი 5 ელემენტი
"""
