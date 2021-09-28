"""
Name: Lesly Endara

lab4.py

certification of Authenticity:
I certify that this is entirely my own work, worked with Jessica, Katie
"""

from math import *
from graphics import *

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(100, 120), Point(150, 170))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shapeCopy = shape.clone()
        shape.move(dx, dy)
        shapeCopy.draw(win)
    instructions.undraw()
    leave = Text(inst_pt, "Click again to quit")
    leave.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    window = GraphWin("rectangle", 400, 400)
    message = Text(Point(200, 300), "select two points for your rectangle")
    message.draw(window)

    point1 = window.getMouse()
    point1.draw(window)
    point2 = window.getMouse()
    point2.draw(window)
    rect = Rectangle(point1, point2)
    rect.setFill("pink")
    rect.draw(window)

    # calculate
    point1_x = point1.getX()
    point1_y = point1.getY()
    point2_x = point2.getX()
    point2_y = point2.getY()

    width = abs(point2_x) - abs(point1_x)
    height = abs(point2_y) - abs(point1_y)

    # area
    area = width * height

    # perimeter
    perimeter = 2 * (width + height)
    print("area:", area)
    print("perimeter:", perimeter)

    message.setText("click to close")
    window.getMouse()
    window.close()


def circle():
    window = GraphWin("circle", 400, 400)
    message = Text(Point(200, 300), "select two points to make a circle")
    message.draw(window)

    pointa = window.getMouse()
    pointb = window.getMouse()

    center_x = pointa.getX()
    center_y = pointa.getY()
    edge_x = pointb.getX()
    edge_y = pointb.getY()
    # radius
    parenthesis1 = (edge_x - center_x) ** 2
    parenthesis2 = (edge_y - center_y) ** 2
    addition = parenthesis1 + parenthesis2
    radius = sqrt(addition)

    circle_ = Circle(pointa, radius)
    circle_.draw(window)
    words = Text(Point(200, 100), radius)
    words.draw(window)
    message.setText("click to close")
    window.getMouse()
    window.close()


def main():
    squares()
    rectangle()
    circle()
    # pi2()


main()
