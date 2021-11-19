"""
Name: Lesly Endara
button.py

create a 3 door, with one secret winner

certification of Authenticity:
I certify that this is entirely my own work
"""

from graphics import GraphWin, Point, Rectangle, Text
from random import randint
from button import Button


def create_square(point_one_x, point_one_y, point_two_x, point_two_y):
    square = Rectangle(Point(point_one_x, point_one_y), Point(point_two_x, point_two_y))
    return square


def make_button(square, label):
    button = Button(square, label)
    return button


def message(center_x, center_y, inside):
    words = Text(Point(center_x, center_y), inside)
    return words


def create_label(square, label, win):
    center = square.getCenter()
    draw_it = Text(center, label)
    draw_it.draw(win)
    return label


def check(button_1, button_2, button_3):
    button_click = bool(button_1 or button_2 or button_3)
    return button_click


def find_click(button1_hit, button2_hit, button_one, button_two, button_three):
    if button1_hit:
        clicked = button_one
    elif button2_hit:
        clicked = button_two
    else:
        clicked = button_three
    return clicked


def winner(random, button_one, button_two, button_three):
    if random == 1:
        wins = button_one
    elif random == 2:
        wins = button_two
    else:
        wins = button_three
    return wins


def second(win_center, click_center, click_button, win_button, win):
    if win_center == click_center:
        click_button.color_button("green")
        message_one = message(7, 8, "you win!")
        message_two = message(7, 2, "click to close")
    else:
        click_button.color_button("red")
        message_one = message(7, 8, "sorry that's wrong")
        message_two = message(7.5, 2, "The correct door is {0}".format(win_button))
    click_button.draw(win)
    message_one.draw(win)
    message_two.draw(win)


def door_name(button1, button2, button3, wins):

    if button1 == wins:
        return str("door 1")
    elif button2 == wins:
        return str("door 2")
    elif button3 == wins:
        return str("door 3")


def main():
    win = GraphWin("Three Door Game", 500, 500)
    win.setCoords(0, 0, 15, 15)
    square_one = create_square(2, 4, 4, 6)
    square_two = create_square(6, 4, 8, 6)
    square_three = create_square(10, 4, 12, 6)
    opening = message(7, 8, "I have a secret door")
    bottom = message(7, 2, "Click to choose my door")

    button_one = make_button(square_one, "Door 1")
    button_two = make_button(square_two, "Door 2")
    button_three = make_button(square_three, "Door 3")
    opening.draw(win)
    bottom.draw(win)
    button_one.draw(win)
    button_two.draw(win)
    button_three.draw(win)

    create_label(square_one, "Door 1", win)
    create_label(square_two, "Door 2", win)
    create_label(square_three, "Door 3", win)

    button_click, button_one_click, button_two_click = False, False, False

    while not button_click:
        point = win.getMouse()
        button_one_click = button_one.is_clicked(point)
        button_two_click = button_two.is_clicked(point)
        button_three_click = button_three.is_clicked(point)
        button_click = check(button_one_click, button_two_click, button_three_click)

    button_is_clicked = find_click(button_one_click, button_two_click, button_one, button_two,
                                   button_three)
    button_is_clicked.undraw()
    opening.undraw()
    bottom.undraw()

    number_rand = randint(1, 3)
    win_button = winner(number_rand, button_one, button_two, button_three)
    winner_line = door_name(button_one, button_two, button_three, win_button)
    win_center = win_button.center()
    clicked_center = button_is_clicked.center()
    second(win_center, clicked_center, button_is_clicked, winner_line, win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()