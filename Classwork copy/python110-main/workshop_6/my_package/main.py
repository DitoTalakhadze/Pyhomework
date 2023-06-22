# import my_module as md
# from my_module import *  # not recommended
from my_module import generate_unique_id


def main() -> None:
    user_id: int = generate_unique_id()
    print(user_id)


if __name__ == '__main__':
    main()
