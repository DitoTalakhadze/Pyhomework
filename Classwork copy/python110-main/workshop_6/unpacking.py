x, y, z = [5, 8, 9]

print(x + y + z)

products: list[tuple[str, int]] = [
    ('Car', 450000),
    ('Car 2', 490000),
    ('Car 3', 850000),
    ('Car 3', 850000)
]

"""
for i, num in enumerate([1, 2, 3, 4]):
    print(i)
"""

for name, price in products:
    # name, price = product
    print(name, price)
