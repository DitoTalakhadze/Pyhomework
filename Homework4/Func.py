#8.1 
def function():
    print("we are learning functions in this chapter")
function()

#8.2
def my_fav_book(book):
    print(f"my favourite book is {book.title()}")
my_fav_book("mysterious island")

def make_shirt(size, text):
    print(f"size of a shirt is {size}, text written on it is: {text}")

make_shirt(22, "howdy ho")


#8.3


def make_shirt(size = "L", text = "I like Py"):
    print(f"size of a shirt is {size}, text written on it is: {text}")

make_shirt()
make_shirt(text = "nomnomnom")

#8.4
def describe_city(city, country = "Georgia"):
    print(F"{city} is in {country}")
describe_city("tbilisi")
describe_city("NYC", country = "USA")


#8.6
def city_country(city, country):
    print(F"{city.title()}, {country.title()}")
city_country("rome", "italy")

    
#8.7 - 8.8

def make_album(name, album, song_count = ""):
    if song_count:
        musician = {"name": name.title(), "album": album.title(), "songs": song_count}
    else:
        musician = {"name": name.title(), "album": album.title()}
    return musician

musician = make_album("johnny", "oh my lord", 666)
print(musician)

