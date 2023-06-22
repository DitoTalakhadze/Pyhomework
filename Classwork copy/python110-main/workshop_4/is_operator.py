"""
is operator compares if objects are the same
id -> returns unique identifier (RAM address)
"""

a = str(5 * 10 ** 20)
b = str(5 * 10 ** 20)

print(f'{a == b = } and {a is b = }')
print(id(a), id(b))
