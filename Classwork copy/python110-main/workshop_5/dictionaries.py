"""
Data Structure - Dict - [Map]
consists key-value pair
"""

person = {
    'name': 'Joe',
    'last_name': 'Doe',
    'age': 27
}

a = None
print(a)

print(f'{person = }')
print(f'{person["name"] = }')
print(person['age'])
# print(person['first_name'])
print(person.get('first_name', 'Unknown User'))
print(f'{bool(None) = }')

person['pet'] = 'Doggo'
person['name'] = 'Lela'
print(f'{person = }')
person.pop('pet')
print(f'after pop {person = }')

person.popitem()
print(f'after pop item {person = }')
person.clear()
print(f'after clear {person = }')

person['car'] = 'hatchback'
print(f'{person = }')
person_new_details = {'car': 'sedan', 'work': 'IT', 'salary': 25000}
person.update(person_new_details)
print(f'{person = }')

print('#' * 5, 'just for loop', '#' * 5)
for key in person:
    print(f'{key = }')

print('#' * 5, 'keys', '#' * 5)
for key in person.keys():
    print(f'{key = } | {person[key] = }')


print('#' * 5, 'values', '#' * 5)
for value in person.values():
    print(f'{value = }')

print('#' * 5, 'items', '#' * 5)
for key, value in person.items():
    print(f'{key = }, {value = }')
