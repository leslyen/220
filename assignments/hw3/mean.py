"""
Name: Lesly Endara
interest.py

Problem: play with ch 4 material


certification of Authenticity:
I certify that this is entirely my own work

1.This program will calculate the mean, Harmonic Mean and the Geometric Mean
2.input the amount of numbers that will be listed, and the list of numbers. Output the different means
What is a step-by-step list of what the program must do, aka an algorithm?  (Remember this is in English!)
"""
import math
def main():
    # ask for input
    amount = eval(input("enter the values to be entered:"))

    # calculate
    rms_sum = 0
    geometric_times = 1
    harmonic_sum = 0
    for number in range(amount):
        value = eval(input("enter value " + str(number + 1) + ":"))
        # rms average
        squared = math.pow(value, 2)
        rms_sum = squared + rms_sum
        # harmonic
        harmonic_division = 1 / value
        harmonic_sum = harmonic_division + harmonic_sum
        # geometric
        geometric_times = value * geometric_times
    # rms
    divided = rms_sum / amount
    rms_total = math.sqrt(divided)
    # harmonic
    harmonic_total = amount / harmonic_sum
    # geometric
    geometric_total = geometric_times ** (1 / amount)
    # display means
    print(round(rms_total, 3))
    print(round(harmonic_total, 3))
    print(round(geometric_total, 3))


if __name__ == "__main__":
    main()
