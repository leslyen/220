"""
Name: Lesly Endara
button.py

create a button

certification of Authenticity:
I certify that this is entirely my own work
"""

from graphics import *
from random import randint


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        center = shape.getCenter()
        self.label = label

    def get_label(self):
        label = self.label
        label = label.getText()
        return label

    def draw(self, win):
        box = self.shape
        box.draw(win)

    def undraw(self):
        box = self.shape
        box.undraw()

    def corners(self):
        button = self.shape
        x_one = button.getP1().getX()
        x_two = button.getP2().getX()
        y_one = button.getP1().getY()
        y_two = button.getP2().getY()
        return x_one, x_two, y_one, y_two

    def center(self):
        button = self.shape
        center = button.getCenter
        return center

    def is_clicked(self, point):
        click_x = point.getX()
        click_y = point.getY()
        x_one, x_two, y_one, y_two = self.corners()
        hit = bool(x_one <= click_x <= x_two and y_one <= click_y <= y_two)
        return hit

    def color_button(self, color):
        color = str(color)
        button = self.shape
        button.setFill(color)

    def set_label(self, label):
        label = self.label
        label = label.getText()
