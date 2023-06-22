"""
Data Types:

* int   - [Z] INTEGER   - მთელი რიცხვები    (-INF, ..., -2, -1, 0, 1, 2, ..., INF)
* float - [Q] FRACTION  - წილადები         (-INF, ..., -2, -1.99, -1.98, 0, 1.98, 1.99, 2, ..., INF)
* str   - String        - ტექსტური დატა
* bool  - Boolean       - True, False
"""


""" Numbers """
age = 27

print(type(age), age)

gas_price_bad = 2.34
print(type(gas_price_bad), gas_price_bad)

gas_price = 10
gas_price = gas_price + 20
print(gas_price / 100)
# print(0.1 + 0.2)  # 0.3

""" String """
first_name = 'John\'s'
last_name = 'Doe'
# bio = '\nthis is my bio\n\nworks at somewhere\n'
bio = f'''
Name: {first_name}
Last Name: {last_name}
this is my bio\t
\t
works at somewhere
'''
print(first_name, last_name)
print(bio)

print(ord('\n'))    # number of this character in ASCII table
print(chr(97))      # returns character from ASCII table

""" Booleans """
is_raining = False
is_windy = True

"""
and
or
not
"""
print(f'{not is_raining = }')  # True
print(f'{not is_windy = }')  # False
# print('not is_raining =', not is_raining)
print(f'{is_raining and is_windy = }')
print(f'{is_raining or is_windy = }')
