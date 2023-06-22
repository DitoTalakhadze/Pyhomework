import random
from typing import Any


def find_number(__number: int, __numbers: list[int]) -> int:
    """
    :param __number: Number to find
    :param __numbers: Where to find this number
    :return: Index of a found number OR -1 if number was not found
    """
    for i, number in enumerate(__numbers):
        if number == __number:
            return i

    return -1


def reorder_list(__list: list[Any]) -> list[Any]:
    """
    reorders lists in such way that values on even and odd indexes are swapped
    EXAMPLE:
    0 -> 1
    1 <- 0
    """
    # When function returns something it is advised that you shouldn't modify parameters
    reordered_list: list[Any] = []
    for i in range(1, len(__list), 2):
        reordered_list.append(__list[i])
        reordered_list.append(__list[i - 1])

    if len(__list) % 2 == 1:
        reordered_list.append(__list[-1])

    # __list.clear()
    # __list.extend(reordered_list)
    # __list = reordered_list
    return reordered_list


def add_random_number_in_list(__list: list[int] = None) -> None:
    if __list is None:
        __list = []

    random_number: int = random.randint(0, 100)
    __list.append(random_number)
    print(__list)


nums_list: list[int] = list(range(0, 11))

print(nums_list)
print(find_number(5, nums_list))
print(find_number(250, nums_list))
r_list: list[int] = reorder_list(nums_list)
print(nums_list)
print(r_list)
print(r_list == nums_list)

print('Default value mutable object (in this case list)')
add_random_number_in_list(nums_list)
add_random_number_in_list()
add_random_number_in_list()
add_random_number_in_list()
