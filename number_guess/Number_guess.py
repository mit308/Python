# creating a random number generator

import random


def guess(x):
    random_number = random.randint(1, x)
    # print(random_number)
    guess_1 = 0
    while guess_1 != random_number:
        guess_1 = int(input(f"Enter the guessing number between 1 to {x} "))
        if guess_1 > random_number:
            print("Too high! Try again")
        elif guess_1 < random_number:
            print("Too low! Try again")
    print(f"Yayyyy you guessed the number right! It is {random_number}, Well done")


# guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # can be high too because low == high
        feedback = input(f'Is {guess} to high (H), too low (L), or correct (C)???').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yayyy the computer guessed the number correctly. The number is {guess}')


computer_guess(10)
