def get_int_from_input() -> int:
    while True:
        try:
            return int(input('Enter an int: '))
        except ValueError:
            print('Please Enter a number')


def some_function():
    num_1: int = get_int_from_input()

    while True:
        num_2: int = get_int_from_input()

        try:
            print(num_1 / num_2)
        except ZeroDivisionError:
            print('You cannot divide number by 0')
        else:
            return
        finally:
            print('I will be executed anyway')


print('Function finished: ', some_function())
