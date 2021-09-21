"""
Name: Lesly Endara
lab2.py

problem: working with loops
"""
import math


def sum_of_threes():
    upper = eval(input("Input an upper bound:"))
    solution = 0
    for bound in range(3, upper + 1, 3):
        solution = solution + 1
        print(solution)
        # end for


def muliplication_table():
    print("1 2 3 4 5 6 7 8 9 10:")
    solution = 0
    for one in range(1, 11, 1):
        solution = one
        print(solution, end=" ")
    print("")
    for two in range(2, 21, 2):
        solution = two
        print(solution, end=" ")
    print("")
    for three in range(3, 31, 3):
        solution = three
        print(solution, end=" ")
    print("")
    for four in range(4, 41, 4):
        solution = four
        print(solution, end=" ")
    print("")
    for five in range(5, 51, 5):
        solution = five
        print(solution, end=" ")
    print("")
    for six in range(6, 61, 6):
        solution = six
        print(solution, end=" ")
    print("")
    for seven in range(7, 71, 7):
        solution = seven
        print(solution, end=" ")
    print("")
    for eight in range(8, 81, 8):
        solution = eight
        print(solution, end=" ")
    print("")
    for nine in range(9, 91, 9):
        solution = nine
        print(solution, end=" ")
    print("")
    for ten in range(10, 101, 10):
        solution = ten
        print(solution, end=" ")
    print("")


def triangle_area():
    a = eval(input("what is side a?:"))
    b = eval(input("what is side b?:"))
    c = eval(input("what is side c?:"))
    # calculate
    calc = (a + b + c)/2
    calctwo = calc * (calc - a) * (calc - b) * (calc - c)
    area = math.sqrt(calctwo)
    print(area)


def sumSquares():
    numbers = 0
    start = eval(input("starting number:"))
    end = eval(input("ending number:"))
    for square in range(start, end + 1):
        numbers += square**2
        print(numbers)


def power():
    base = eval(input("enter base:"))
    elevated = eval(input("enter the power"))
    solution = 1
    for total in range(elevated):
        solution = solution * base
    print(base, "^", elevated, "=", solution)

muliplication_table()
power()