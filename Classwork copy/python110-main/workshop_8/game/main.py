"""
There are files in levels directory (Folder)
program should prompt user and ask which level should be loaded
levels start from 0 and go up to 10
* levels are 2D (dimensional)
* application should draw this maps to the screen
* user cannot move on cells that have value of 1
* user should be able to move on cells where value is 0
* there are collectable items
    - 5 == COIN
    - 6 == GOLD BAG (10 COINS)
* user should also be careful since there are holes in map
    - 7 == hole
* count how many moves did user make
* at the end of game ask user for name
* save high score in file
* user starts at upper left most corner
"""
import os.path

"""
Program layout:

Problems:
* how to save this map in memory
    - 2D list
* how to control map state (remove collectables from screen)
    - user coordinates (x, y)
* user state
    - if user died
    - coins
* render (how to draw the map)
    - nested for loop
* input (user movement)
    - 'w' - (x, y - 1)
    - 's' - (x, y + 1)
    - 'a' - (x - 1, y)
    - 'd' - (x + 1, y)

Game flow:
1. ask user which level should be loaded
2. [Loop] Game Loop
    2.1 Draw map
    2.2 Get user input (decide movement)
    2.3 Update user coordinates
    2.4 Check user state (collectable or danger)
        2.4.1 if all collectables are collected WIN
        2.4.2 if danger LOSE
    2.5 Update map (remove coins from map)
3. ask user for name
4. save high score in files
"""
DANGER = [1, 7]


class Player:
    def __init__(self) -> None:
        self.x = 1
        self.y = 1
        self.coins = 0
        self.moves = 0

    def move(self) -> None:
        while True:
            direction: str = input('Where? ').lower()

            if direction == 'w':
                self.y -= 1
            elif direction == 's':
                self.y += 1
            elif direction == 'a':
                self.x -= 1
            elif direction == 'd':
                self.x += 1
            else:
                print('(w/a/s/d)')
                continue

            self.moves += 1
            return

    def check_current_cell(self) -> None:
        global is_running
        cell: int = level[self.y][self.x]

        if cell in DANGER:
            is_running = False
            if cell == 7:
                print('aaaaaaah')
            else:
                print('You bumped your head too strong to wall')
            return

        if cell == 5:
            self.coins += 1
        elif cell == 6:
            self.coins += 10

    def won_the_game(self) -> bool:
        for row in level:
            if 5 in row or 6 in row:
                return False
        return True


def select_level() -> str:
    while True:
        selected_level = input('Enter Level [1 - 9]: ')
        level_name = f'./levels/level_0{selected_level}.map'
        print(level_name)
        if os.path.exists(level_name):
            return level_name

        print('Please selected valid level!')


def render_map() -> None:
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if player.x == x and player.y == y:
                print('P', end='')
            else:
                if cell == 1:
                    print('#', end='')
                elif cell == 5:
                    print('*', end='')
                elif cell == 6:
                    print('@', end='')
                elif cell == 0:
                    print(' ', end='')
                else:
                    print('o', end='')
        print()


def build_level(__level_path: str) -> list[list[int]]:
    _level: list[list[int]] = []
    with open(__level_path) as f:
        for line in f.readlines():
            _level.append(
                [
                    int(cell)
                    for cell in line.strip()
                ]
            )

    return _level


def update_map() -> None:
    level[player.y][player.x] = 0


def clear_screen() -> None:
    print('\033c')


is_running: bool = True
player: Player = Player()
with open('high_score.txt') as f:
    print('Leader Board')
    print(f.read())
level_path: str = select_level()
level: list[list[int]] = build_level(level_path)

if __name__ == '__main__':
    print(f'User selected: {level_path}')
    while is_running:
        clear_screen()
        print(f'Current Coins: {player.coins}')
        print(f'Current Moves: {player.moves}')
        render_map()
        player.move()
        player.check_current_cell()
        update_map()
        if player.won_the_game():
            print(f'You won the game in {player.moves} moves')
            break

    username = input('Name: ')

    with open('high_score.txt', 'a+') as f:
        f.write(f'{username} - {level_path} - {player.moves} - {player.coins}\n')
