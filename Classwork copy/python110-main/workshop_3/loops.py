"""
Loops - Repeating same code

"""

users = ['Joe', 'Jane', 'James', 'Janet', 'Joe']

for user in users:  # iterate through list elements
    # code fragment
    print(f'Hello {user}')
    print('next user please!')
# print('Done')


# for i in range(10):
#     print(f'sorry {i}')

# for i in range(len(users)):
#     print(users[i])

for i, user in enumerate(users):
    print(f'element\'s value at index {i} is: {user}')

