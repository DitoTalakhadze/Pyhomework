import random

random_number = random.randint(1, 99)

while True:
    guess = int(input("Guess a number between 1 and 99: "))

    if guess < random_number:
        print("Too low! Guess higher.")
    elif guess > random_number:
        print("Too high! Guess lower.")
    else:
        print("Congratulations! You guessed the number correctly.")
        break
