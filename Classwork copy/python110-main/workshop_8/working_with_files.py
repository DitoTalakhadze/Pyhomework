import time
import os

if os.path.exists('user.txt'):
    print('File exists')
    with open('user.txt', 'r+') as f:
        user = f.read()
else:
    user = ""

# try:
#     with open('user.txt', 'r+') as f:
#         user = f.read()
# except FileNotFoundError:
#     user = ""

print(f'User from file: "{user}"')
if not user:
    user: str = input('Enter your name: ')  # Save in RAM / Temporary memory

# f = open('user.txt', 'w')
# f.write(user)
# f.close()

with open('user.txt', 'w') as f:
    # context manager
    f.write(user)

print(user)
