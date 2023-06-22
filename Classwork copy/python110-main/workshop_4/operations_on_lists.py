"""
List Comprehension - Generators
"""


"""
nums = [
    num
    for num in range(100)
]
"""

"""
nums = []
for num in range(100):
    nums.append(num)
"""

nums = list(range(0, 20, 1))

even_nums = [
    num
    for num in nums
    if num % 2 == 0
]

odd_nums = [
    num
    for num in nums
    if num % 2 == 1
]

nums_divisible_by_3 = [
    num
    for num in nums
    if num % 3 == 0
]

"""
even_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

nums = even_nums
"""

print(nums)
print(f'{even_nums = }')
print(f'{odd_nums = }')
print(f'{nums_divisible_by_3 = }')

print(f'{nums_divisible_by_3[::2] = }')

nums_divisible_by_3_copy = nums_divisible_by_3[:]
print(f'{nums_divisible_by_3_copy == nums_divisible_by_3 = }')
print(f'{nums_divisible_by_3_copy is nums_divisible_by_3 = }')
# print(f'{id(nums_divisible_by_3)} {id(nums_divisible_by_3_copy)}')

# nums_divisible_by_3.reverse()
print(f'{nums_divisible_by_3[::-1] = }')

# print(list(range(100, 0, -1)))
