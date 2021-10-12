"""
Name: Lesly Endara
Partner: Jessica
lab7.py
"""

from math import *

def cash_conversion():
    amount = eval(input("what will the integer be?"))
    print("$" + "{0:0.2f}".format(amount))


def encode():
    words = input("which message would you like to encode")
    number = eval(input("what will your key value be?"))
    secret_word = ""
    for count in words:
        convert = ord(count) + number
        character = chr(convert)
        print(character, end="")
    print("")


def sphere_area(radius): #-> surface_area
    area = 4 * pi * pow(radius, 2)
    return(area)


def sphere_volume(radius): #-> volume
    volume = 4 / 3 * pi * pow(radius, 3)
    return(volume)

def sum_n(n):
    temp = n
    for count in range(n):
        temp += count
    return(temp)

def sum_n_cubes(n): #-> total
    temp = n
    add = 0
    for count in range(n):
        cubed = pow(count + 1, 3)
        add += cubed
    return(add)

def encode_better():
    words = str(input("which message would you like to encode"))
    key = str(input("what will your key value be?"))
    secret_word = ""
    for count in range(len(words)):
        convert = ord(key[count]) - 97
        second_cov = ord(words[count]) + convert
        character = chr(second_cov)
        secret_word += character
    print(secret_word)


def main():
    # add function calls here
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(2))
    print(sum_n(5))
    print(sum_n_cubes(2))
    encode_better()


main()
