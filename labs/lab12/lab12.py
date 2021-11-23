"""
Name: Lesly Endara
lab12.py
create a hangman game
certification of Authenticity:
I certify that this is entirely my own work
"""
import algorithms
from random import randint

"""
def read_data(filename):
    inside = open(filename, "r")
    parts = inside.read()
    numbers = parts.split()
    list = []
    i = 0
    while i < len(numbers):
        new_list = eval(numbers[i])
        list.append(new_list)
        i += 1
    inside.close()
    return list


def is_in_linear(search_val, values):
    i = 0
    answer = False
    try:
        while i < len(values):
            parts = values.index(search_val)
            if values[parts] == search_val:
                answer = True
            i += 1
    except:
        answer = False
    return answer
"""

def find_and_remove_first(list, value):
    part = list.index(value)
    list.remove(value)
    list.insert(part, "Lesly")
    print(list)

def good_input():
    number = eval(input("please enter a number from 1-10"))
    while number >= 10 or number <= 1:
        if number >= 10:
            number = eval(input("the input is too large, try again"))
        elif number <= 1:
            number = eval(input("the input is too small, try again"))
    print("yay, you entered", number, "thank you")
    return number

def  num_digits():
    number = eval(input("please enter a positive number"))
    while number >= 0:
        times = 0
        while number > 0:
            number = number // 10
            times += 1
        print(times)
        number = eval(input("please enter a positive number"))


"""
def hi_lo_game():
    number = randint(1, 100)
    guess = eval(input("try to guess my number (it's between 1-100"))
    while guess > number or guess < number:
        if guess > number:
            guess = eval(input(""))
            didn't get to it
"""


def main():
    parts = [1, 2, 3, 1, 5, 8, 6, 5]
    find_and_remove_first(parts, 5)
    name = "read_data_test_data.txt"
    file_list = algorithms.read_data(name)
    print(file_list)
    print(algorithms.is_in_linear(79, file_list))
    good_input()
    num_digits()

    pass


main()