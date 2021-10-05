"""
Name: Lesly Endara
greeting.py

Problem: draw a heart with a moving arrow :'(

certification of Authenticity:
I certify that this is entirely my own work
"""
import time

from graphics import *

def main():
    win = GraphWin("heart", 400, 400)
    width = 400
    height = 400

    # heart
    circ = Circle(Point(125, 150), 70)
    circ_two = Circle(Point(250, 150), 70)
    circ.draw(win)
    circ_two.draw(win)
    triangle = Polygon(Point(57, 170), Point(190, 350), Point(318, 170))
    triangle.setFill("red"), circ.setFill("red"), circ_two.setFill("red")
    triangle.setOutline("red"), circ_two.setOutline("red"), circ.setOutline("red")
    triangle.draw(win)
    message_box = Point(width / 2, height / 2)
    message = Text(message_box, "Happy Valentine’s Day!")
    message.setSize(20)
    message.setFace("courier")
    message.draw(win)
    time.sleep(4)
    message.undraw()

    # arrow
    arrow_body = Line(Point(50, 350), Point(100, 250))
    arrow_body.setWidth(3), arrow_body.setOutline("brown")
    arrow_head = Polygon(Point(90, 245), Point(110, 255), Point(105, 240))
    arrow_head.setFill("grey")
    arrow_head.draw(win), arrow_body.draw(win)

    for movement in range(20):
        arrow_body.move(5, -5)
        arrow_head.move(5, -5)
        time.sleep(0.1)
    arrow_head.undraw()
    up = circ_two.clone()
    up.draw(win)

    box = Point(width / 2, height - 10)
    letter = Text(box, "Click anywhere to close")
    letter.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
