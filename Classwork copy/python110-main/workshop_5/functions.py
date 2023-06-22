"""
Functions
block of code (code fragment) that executes only when it is called
"""
# global scope
name = 'Joe'
a = 1


# function definition
def add(a: int, b: int):
    # local scope
    # name shadowing
    print(a + b)

# positional arguments
add(6, 5)  # function call
# keyword arguments
add(a=7, b=8)  # function call
add(7, 8)
add(b=8, a=7)


def greet(username: str = 'Unknown User', greeting_word: str = 'Hello'):
    # default value
    # positional parameter should be before default value
    print(f'{greeting_word} {username}')


greet(name)
greet('Nick')
greet('Mark')
greet(greeting_word='გამარჯობა')
