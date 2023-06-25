def my_func(*args: int, **kwargs: int) -> None:
    if len(args) < 2:
        raise Exception("I need at least 2 parameters")
    print(args, kwargs)


my_kwargs: dict[str, int] = {"a": 8, "b": 9}

nums: list[int] = [2, 5, 8, 5, 6, 3, 2]

my_func(2, 5, 8, 5, 6, 3, 2, a=8, b=9)
my_func(*nums, **my_kwargs)

print(*nums)
