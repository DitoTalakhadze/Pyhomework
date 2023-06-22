first_name = 'John'
age = 55

"""
Comparison Operators:

==  - Equality
!=  - Inequality
>   - Greater than
>=  - Greater than or equal to
<   - Less than
<=  - Less than or equal to
"""
print(age % 2 == 1)  # True
if age % 2 == 1 and first_name == 'John':
    # indentation
    # code fragment
    print('პირობა დაკმაყოფილდა')
elif age % 4 == 0 or first_name == 'gio':
    print('Wow')
else:
    print('პირობა არ დაკმაყოფილდა')

# hard coding
user = 'Jack'
password = 'Jack123'

if user == 'Jack' and password == 'Jack123':
    print('User logged in')
else:
    print('Authentication failed!')

if user == 'Jack':
    print('You have a coupon')
