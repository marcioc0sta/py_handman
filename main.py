import random
from words import word_list
from hangmanDisplay import display_hangman


def get_words():
    word = random.choice(word_list)
    return word.upper()


def feedback(message, tries, word_completion):
    print("H A N G M A N")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')


def decrease_tries(tries, guessed_letters, guess):
    print('Your guess is not in the word')
    tries -= 1
    guessed_letters.append(guess)


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    feedback('H A N G M A N', tries, word_completion)

    while not guessed and tries > 0:
        guess = input('Please guess a letter or a word').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed this letter', guess)

            elif guess not in word:
                decrease_tries(tries, guessed_letters, guess)

            else:
                print(f'Good job {guess}  is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess]

                for index in indexes:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        # elif len(guess) == len(word) and guess.isalpha():

        else:
            feedback('Wrong guess!', tries, word_completion)