"""
Data Structure - List - Array - მასივი
help us to save many objects in single variable
"""
#              0      1        2        3       4
usernames = ['Joe', 'Jane', 'James', 'Janet', 'Joe']
ages = [27, 31, 41, 23, 66]

print(usernames, len(usernames))
print(ages, len(ages))

# index
# accessing elements by index
print('#' * 5, ' Access ', '#' * 5)
print(f'First element of usernames list is "{usernames[0]}" and age is {ages[0]}')

# search
print('#' * 5, ' Search ', '#' * 5)
print(f'Index of value "Joe" is {usernames.index("Joe")}')
print(f'Is Nick in the list? {"Nick" in usernames}')

# add new elements
print('#' * 5, ' Add ', '#' * 5)
usernames.append('Nick')
ages.append(19)

print(usernames)
print(f'Is Nick in the list [in operator]? {"Nick" in usernames}')

# insert method at specific index
usernames.insert(1, "Gela")
ages.insert(1, 45)
print(f'usernames after inserting at index 1 {usernames}')
print(f'ages after inserting at index 1 {ages}')


# remove elements
print('#' * 5, ' Remove ', '#' * 5)
usernames.pop()  # returns removed element!
ages.pop()
print(f'usernames after popping {usernames}')
print(f'ages after popping {ages}')

usernames.pop(1)
ages.pop(1)
print(f'usernames after popping {usernames}')
print(f'ages after popping {ages}')


# Change / Update elements
print('#' * 5, ' Update ', '#' * 5)
usernames[4] = 'John'
ages[4] = 96
print(f'usernames after updating element at index 4: {usernames}')
print(f'ages after updating element at index 4: {ages}')


# Last element
print('#' * 5, ' Last element and Negative index ', '#' * 5)
print(f'Last element is: {usernames[len(usernames) - 1]} {ages[-1]} years old')
