# type casting

def get_int_input(__prompt: str) -> int:
    age = int(input(__prompt))
    return age


def beautify_input() -> str:
    return input('Enter your name: ').title()


def give_me_one() -> int:  # განსაზღვრა
    return 1  # სადაც ფუნქციის გამოძახებაა იქ დააბრუნებს ამ მნიშვნელობას


my_number = give_me_one()  # Function Call / გამოძახება!
print(my_number)

age: int = get_int_input('Enter your age: ')


print(age, type(age))


name = beautify_input()
print(name)
