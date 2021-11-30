"""
Name: Lesly Endara
lab13.py
last lab
certification of Authenticity:
I certify that this is entirely my own work: with Jessica :)
"""
import algorithms
from graphics import Rectangle, Point


def trade_alert(filename):
    opened = open(filename, 'r')
    reader = opened.read()
    reader = reader.split(" ")
    new_file = []
    index = 0
    for i in range(len(reader)):
        numbers = eval(reader[i])
        if numbers > 830:
            print("hey, this is over 830, it's at", i + 1)
        elif numbers == 500:
            print("dude, pay attention, we're getting too close, it's", i + 1)


def main():
    # add other function calls here
    lists = [1, 3, 5, 9, 20, 38, 55, 68, 69, 99]
    unsorted = [7, 5, 9, 4, 85, 533, 8, 3, 1, 9, 980]
    trade_alert("trades.txt")
    algorithms.is_in_binary(20, lists)
    algorithms.selection_sort(unsorted)
    rect = Rectangle(Point(30, 20), Point(40, 50))
    algorithms.calc_area(rect)
    rectangles = [(Rectangle(Point(37, 78), Point(10, 58))), (Rectangle(Point(30, 20), Point(40, 50))),
                                                             (Rectangle(Point(74, 76), Point(41, 59)))]
    new_rectangles = []
    for i in range(len(rectangles)):
        areas = algorithms.calc_area(rectangles[i])
        new_rectangles.append(areas)
    algorithms.rect_sort(new_rectangles)
    pass


main()
