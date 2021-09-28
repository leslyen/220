"""
Name: Lesly Endara
interest.py

Problem: play with ch 4 material


certification of Authenticity:
I certify that this is entirely my own work
"""


def main():
    add = 0

    roads = eval(input("How many roads were surveyed?"))
    for number in range(roads):
        days = eval(input("How many days was road " + str(number + 1) + " surveyed? "))
        for number_days in range (days):
            cars = eval(input("How many cars traveled on day " + str(number_days + 1) + "? "))
            add = cars + add
        average = add / days
        print(average)


if __name__ == "__main__":
        main()

