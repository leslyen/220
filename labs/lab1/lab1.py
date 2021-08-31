"""
Name: Lesly Endara
lab1.py
Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def shooting_percentage():
    total = eval(input("what is the player's total shots:"))
    made = eval(input("How many shots were made:"))
    percentage = (total * 100) / made
    print("the shooting percentage is:", percentage)


def coffee_cost():
    pounds = eval(input("How many pounds have been purchased?"))
    coffee_cost = 10.50 * pounds
    shipping_cost = 0.86 * pounds
    fixed_cost = 1.50
    total_cost = coffee_cost + shipping_cost + fixed_cost
    print("The total cost will be", total_cost)


def kilometers_to_miles():
    number_of_kilometers = eval(input("How many kilometers have you traveled?"))
    conversion = number_of_kilometers / 1.61
    print("you've traveled", conversion, "miles")

