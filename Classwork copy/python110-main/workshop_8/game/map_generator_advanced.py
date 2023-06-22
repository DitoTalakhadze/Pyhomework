import random


def get_cell():
    if random.randint(0, 100) < 80:
        return 0

    return random.choice([1, 5, 6, 7])


def generate_empty_map():
    return ([[1] * 10]) + ([[1] + ([get_cell() for _ in range(8)]) + [1] for _ in range(8)]) + ([[1] * 10])


for i in range(1, 10):
    with open(f'levels/level_0{i}.map', 'w') as f:
        f.write('\n'.join([
            ''.join([str(cell) for cell in row])
            for row in generate_empty_map()
        ]))
