"""
Name: Lesly Endara

lab5.py

certification of Authenticity:
I certify that this is entirely my own work
"""
import gettext

from graphics import *
from math import *

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    first = win.getMouse()
    first.draw(win)
    second = win.getMouse()
    second.draw(win)
    third = win.getMouse()
    third.draw(win)
    picture = Polygon(first, second, third)
    picture.draw(win)
    picture.setFill("blue")

    # calculate
    xOne = first.getX()
    xTwo = second.getX()
    xThree = third.getX()
    yOne = first.getY()
    yTwo = second.getY()
    yThree = third.getY()

    dx_one = xTwo - xOne
    dy_one = yTwo - yOne

    length_one = sqrt(pow(dx_one, 2) + pow(dy_one, 2))

    dx_two = xThree - xTwo
    dy_two = yThree - yTwo

    length_two = sqrt(pow(dx_two, 2) + pow(dy_two, 2))

    dx_three = xThree - xOne
    dy_three = yThree - yOne

    length_three = sqrt(pow(dx_three, 2) + pow(dy_three, 2))

    perimeter = (length_one + length_two + length_three)

    s = perimeter / 2
    area = sqrt(s *(s - length_one) * (s - length_two) * (s - length_three))

    # and display its area in the graphics window.
    areaText = Text(Point(200, 50), "area: " + str(round(area, 2)))
    perimeterText = Text(Point(200, 100), "perimeter: " + str(round(perimeter, 2)))
    areaText.draw(win)
    perimeterText.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    box_point = Point(win_width / 2 - 10, win_height / 2 + 40)
    red_box = Entry(box_point, 5)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_box_pt = box_point.clone()
    green_text_pt.move(0, 30)
    green_box_pt.move(0, 30)
    green_box = Entry(green_box_pt, 5)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_box_pt = box_point.clone()
    blue_text_pt.move(0, 60)
    blue_box_pt.move(0, 60)
    blue_box = Entry(blue_box_pt, 5)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    red_box.draw(win)
    green_text.draw(win)
    green_box.draw(win)
    blue_text.draw(win)
    blue_box.draw(win)

    for input in range(0, 5):
        win.getMouse()
        red = red_box.getText()
        green = green_box.getText()
        blue = blue_box.getText()
        true_color = color_rgb(eval(red), eval(green), eval(blue))
        shape.setFill(true_color)
        #close loop

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    word = input("enter a word: ")
    section = len(word)
    print(word[0])
    print(word[- 1])
    print(word[1], word[2], word[3], word[4])
    print(word[0], word[-1])
    print((word[0], word[1], word[2]) * 10)
    count = len(word)
    letter = 0
    for number in range(count):
        print(word[letter])
        letter = letter + 1
    print(count)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt,"7.2"]
    x = ("hi" + "there")
    print(x)
    x = (5 + 2.5)
    print(x)
    x = ("hi" * 5)
    print(x)
    x = [2.5, "there", pt]
    print(x)
    x = [2.5, "there", 5]
    print(x)
    x = [2.5, 5, 7.2]
    print(x)
    x = [5 + 2.5 + 7.2]
    print(x)
    x = len(values)
    print(x)


def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    pass


main()
