"""
Name: Lesly Endara
interest.py

Problem: ask for the amount of cars that drive on a daily basis on different
roads. and give out the average and sum.

certification of Authenticity:
I certify that this is entirely my own work
"""


def main():
    add = 0
    total = 0
    total_add = 0
    roads = eval(input("How many roads were surveyed?"))
    for number in range(roads):
        days = eval(input("How many days was road " + str(number + 1) + " surveyed? "))
        for number_days in range(days):
            cars = eval(input("How many cars traveled on day " + str(number_days + 1) + "? "))
            add = cars + add
        average = add / days
        total = add + total
        total_add = add + total_add
        print("average vehicles per day: ", round(average, 2))
        add = 0

    total_average = total_add / roads
    # --Display--
    print("Total number of vehicles traveled on all roads: ", total)
    print("Average number of vehicles per road: ", round(total_average, 2))

if __name__ == "__main__":
        main()


