# rock paper scissor

import random

'''

def rps():
    play = ''
    while play != 'n':
        play = input("Enter y if you want to play else n to exit ").lower()
        number = random.randint(1, 3)
        if number == 1:
            print("Stone")
        elif number == 2:
            print("Paper")
        elif number == 3:
            print("Scissor")
rps()
'''


def play():
    user = input("Enter your choice for r, s, p ")
    computer = random.choice(['r', 's', 'p'])
    if user == computer:
        return 'tie'

    if is_won(user, computer):
        return 'You Won!!!!'

    return 'Sorry You Lost!!'


# r>s, s>p, p>s  r=rock, s=scissors, p=papers
def is_won(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 's'):
        return True


print(play())
