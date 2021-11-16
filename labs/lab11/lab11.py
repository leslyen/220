"""
Name: Lesly Endara
lab11.py
create a hangman game
certification of Authenticity:
I certify that this is entirely my own work
"""

from random import randint

def pull_words():
    words = open("wordslist.txt", 'r')
    word = words.readlines()
    words.close()
    return word


def random_words(word):
    words = str(word[randint(0, 42)])
    return words


"""
def win(underscores):
    for i in range(len(underscores)):
        if underscores[i] != "_":
            return True
        else:
            return False
            
I could not get to it in time
"""


def guess(word, letter, underscores):
    count = 0
    dash = len(word) - 1
    print(word)
    print("the word is")
    result = word.find(letter)
    word = list(word)
    for i in range(len(word)):
        letter = word[result]
        if letter == word[i]:
            underscores[i] = letter
        else:
            if count <= 7:
                print("sorry you lost a life")
            else:
                print("game over")
                return
    print(str(underscores))
    return underscores


def play():
    pull = pull_words()
    check = random_words(pull)
    underscores = []
    for i in range(len(check) - 1):
        underscores.append("_")
    print(underscores)
    print('')
    print("hi, it's time to play squid games season 2")
    guesses = input("what letter do you think is in this word?")
    guesses.lower()
    while guesses == guesses:
        guess(check, guesses, underscores)
        guesses = input("what letter do you think is in this word?")
        guesses.lower()




def main():
    # add other function calls here
    pull = pull_words()
    check = random_words(pull)
    play()
    pass


main()
