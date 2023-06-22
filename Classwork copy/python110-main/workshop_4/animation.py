"""
While loop
"""
import time

# for i in range(0, 100, 1):
#     print(f'Iteration {i}')

"""
i = 0
while i < 100:
    print(f'Iteration {i}')
    i += 1
"""

standing = '''
 O
/|\\
/ \\
'''

moving = '''
 O
\|/
/ \\
'''

print(standing)
print(moving)

while True:
    print('\033c')
    print(standing)
    time.sleep(1)
    print('\033c')
    print(moving)
    time.sleep(1)



