_sum = 0

# sum of 1 - 100_000
for i in range(1, 100_001, 2):
    # if i % 2 == 1:
    #     _sum += i
    _sum += i

print(_sum,
      (100_000 / 2) * (100_000 + 1))
