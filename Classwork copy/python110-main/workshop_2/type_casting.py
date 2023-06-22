age_in_str = "27"
print(age_in_str, type(age_in_str))

# type casting: str -> int
age = int(age_in_str)

print(age, type(age))
print(str(age) + 'hello')
print(f'{age} hello')

my_float = float('27.9')
print(my_float, type(my_float))


print(str(27.9), type(str(27.9)))

# Truthy / Falsy
print(bool(1), bool(-1), bool(0), bool(-1000))
print(bool("1"), bool("hello"), bool("g"), bool(""))
