product = {
    'title': 'Laptop',
    'price': 3499,
    'brand': 'Asus',
    'previous_owners': [
        'Joe', 'John', 'Jake'
    ]
}

print(product['previous_owners'][-1])
products = [
    {
        'title': 'Laptop',
        'price': 13499,
        'brand': 'Asus',
        'specifications': {
            'ram': [16, 16],
            'cpu': {
                'brand': 'intel',
                'model': 'i9-12900FK'
            }
        }
    },
    {
        'title': 'Laptop',
        'price': 5499,
        'brand': 'Legion',
        'specifications': {
            'ram': [16, 16],
            'cpu': {
                'brand': 'intel',
                'model': 'i9-12900FK'
            }
        }
    },
    {
        'title': 'Laptop',
        'price': 7499,
        'brand': 'Alienware',
        'specifications': {
            'ram': [16, 16],
            'cpu': {
                'brand': 'intel',
                'model': 'i9-12900FK'
            }
        }
    },
]

print(products[1]['title'])
for _product in products:
    print(f"{_product['brand']} has {_product['specifications']['cpu']['model']} and costs {_product['price']}")

highest = products[0]

for product in products[1:]:
    if product['price'] > highest['price']:
        highest = product

print(highest)
