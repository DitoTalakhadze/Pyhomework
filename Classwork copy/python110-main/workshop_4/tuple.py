"""
Tuple - Data Structure

immutable

Immutability - cannot be modified
"""
import sys

fruits = ('Apple', 'Banana', 'Pineapple', 'Orange')
# fruits[0] = 'Watermelon'

print(f'{type(fruits) = }, {fruits}')
print(f'{len(fruits) = }')
for fruit in fruits:
    print(fruit)


nums = tuple(range(20000000))
nums_list = list(range(20000000))
print(sys.getsizeof(nums) / 1000 / 1000)
print(sys.getsizeof(nums_list) / 1000 / 1000)
