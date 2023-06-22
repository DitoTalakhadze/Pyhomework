maze = [
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 5, 1, 1]
]


name = input('Enter you name: ')
# age = int(input('What is your age? '))
cp = (2, 2)  # Current Position of the user
print(f'Welcome {name} to our maze')
while True:
    # Drawing Maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if (y, x) == cp:
                # თუ კოორდინატები ემთხვევა user -ის კოორდინატებს მაშინ დაიხატოს X-ი
                print('X', end='')
                continue

            print(cell, end='')
        print()

    # Getting command from user
    next_move = input('What is your next move? ')

    if next_move == 'up':
        dy = cp[0] - 1
        x = cp[1]
        cell = maze[dy][x]
        if dy < 0 or dy > len(maze) - 1 or cell == 1:
            print('You cannot make that move')
        else:
            cp = (dy, x)
    elif next_move == 'down':
        pass
    elif next_move == 'left':
        y = cp[0]
        dx = cp[1] - 1
        cell = maze[y][dx]
        row = maze[y]
        if dx < 0 or dx > len(row) - 1 or cell == 1:
            print('You cannot make that move')
        else:
            cp = (y, dx)
    elif next_move == 'right':
        pass
    else:
        pass


