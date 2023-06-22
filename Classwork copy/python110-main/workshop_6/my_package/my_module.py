import random


def generate_unique_id() -> int:
    return random.randint(0, 10000000000)


# Guard clause
if __name__ == '__main__':
    print(generate_unique_id())
