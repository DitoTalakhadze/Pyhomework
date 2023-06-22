import random
is_raining = True

while is_raining:
    random_number = random.randint(0, 100)

    if random_number == 50:
        print('Rain Stopped')
        is_raining = False
        break

    if random_number > 50:
        print('Heavy Rain')
        continue

    print('Rain Paused')
