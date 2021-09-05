import random

from words_hangman import words
import string

lives = 7


def choose_a_word(words):
    word = random.choice(words)  # randomly chooses words from the list we have
    while ' ' in words or '-' in words:
        word = random.choice(words)

    return word.upper()


def hangman():
    global lives
    word = choose_a_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # imports upper characters in the pre defined ie the dictionary
    used_letters = set()  # for used letters which user guessed
    while len(word_letters) > 0 and lives != 0:  # will run till word_letters does not become zero
        # used letters
        print("You have used this letters: ", ''.join(used_letters), "You have lives left:", lives)
        # print(word_letters)
        # current word with _ so that they know what is left to be guessed
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current Word: ", ''.join(word_list))
        # print(used_letters)
        # print(alphabet)

        user_letter = input("Enter the letter: \n").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # print(word_letters)
            else:
                lives = lives - 1
                # print("Your lives left are: ", lives)
                print("Oops! the letter is not in the word")

        elif user_letter in used_letters:
            print('You have already used the word! Try again, Your lives left are: ', lives)
        else:
            print('Invalid guess')

    if lives == 0 and len(word_letters) > 0:
        print("BOOM HANGMAN, YOU DIED")
    else:
        print("The word you guessed is ", word, "!!!!!!")

hangman()
