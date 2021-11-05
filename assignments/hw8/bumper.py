"""
Name: Lesly Endara
bumper.py

create a window with 2 bumpers(circles) that change direction
after hitting a wall or each other

certification of Authenticity:
I certify that this is entirely my own work
"""
import time
from random import randint
from graphics import Circle, Point, GraphWin, color_rgb
from math import sqrt


def get_random(move_amount):
    move = randint(-move_amount, move_amount)
    return move


def did_collide(circle_ball, circle_ball2):
    # get centers
    center_x = circle_ball.getCenter().getX()
    center_y = circle_ball.getCenter().getY()
    center_two_x = circle_ball2.getCenter().getX()
    center_two_y = circle_ball2.getCenter().getY()

    # get radius
    radius_one = circle_ball.getRadius()
    radius_two = circle_ball2.getRadius()

    # math
    substract_y = center_two_y - center_y
    substract_x = center_two_x - center_x
    sum_radius = radius_one + radius_two
    # distance formula
    distance = sqrt((substract_x ** 2) + (substract_y ** 2))
    if distance <= sum_radius:
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    centerx = circle_ball.getCenter().getX()
    radius = circle_ball.getRadius()
    if (centerx + radius) >= win.getWidth() or (centerx - radius) <= 0:
        return True
    else:
        return False


def hit_horizontal(circle_ball, win):
    centery = circle_ball.getCenter().getY()
    radius = circle_ball.getRadius()
    if (centery + radius) >= win.getHeight() or (centery - radius) <= 0:
        return True
    else:
        return False


def get_random_color():
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def main():
    # create a window
    width = randint(300, 600)
    height = randint(300, 600)
    win = GraphWin("bumper", width, height)
    win.setBackground(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))

    # create a circle
    circ = Circle(Point(randint(100, 150), randint(200, 300)), 40)
    circ.setFill(get_random_color())
    circ.draw(win)
    moves = 10
    circ2 = Circle(Point(randint(200, 300), randint(100, 200)), 40)
    circ2.setFill(get_random_color())
    circ2.draw(win)

    # get the random parts
    x_one = get_random(moves)
    x_two = get_random(moves)
    y_one = get_random(moves)
    y_two = get_random(moves)

    circ.move(x_one, y_one)
    time.sleep(.01)
    circ2.move(x_two, y_two)
    time.sleep(.01)

    while not(win.checkMouse()):
        circ.move(x_one, y_one)
        time.sleep(.01)
        circ2.move(x_two, y_two)
        time.sleep(.01)
        if hit_vertical(circ, win) is True:
            x_one *= -1
        if hit_horizontal(circ, win) is True:
            y_one *= -1
        if hit_vertical(circ2, win) is True:
            x_two *= -1
        if hit_horizontal(circ2, win) is True:
            y_two *= -1
        if did_collide(circ, circ2) is True:
            x_one *= -1
            y_one *= -1
            y_two *= -1
            x_two *= -1
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
