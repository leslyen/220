"""
Name: Lesly Endara
vigenere.py

create a vigenere encryption using a keyword

certification of Authenticity:
I certify that this is entirely my own work
"""

from graphics import *


def code(message, keyword):
    get_message = message.getText()
    get_key = keyword.getText()
    message_no_space = get_message.replace(" ", "")
    key_no_space = get_key.replace(" ", "")
    capital_message = str.upper(message_no_space)
    capital_key = str.upper(key_no_space)
    secret_word = ""
    for count in range(len(capital_message)):
        convert = ord(capital_key[count % len(capital_key)]) - ord("A")
        second_cov = (ord(capital_message[count]) - ord("A") + convert) % 26 + ord("A")
        character = chr(second_cov)
        secret_word += character
    return secret_word


def draw():
    width = 400
    height = 300
    win = GraphWin("Vigenere", width, height)
    win.setCoords(0.0, 0.0, 3.0, 6.0)

    # text boxes
    message_text = Point(0.5, 5)
    key_text = Point(0.5, 4)
    message_text = Text(message_text, "Message to code")
    key_text = Text(key_text, "Enter keyword")
    message_text.draw(win)
    key_text.draw(win)

    # button
    outline = Rectangle(Point(2, 2), Point(1, 1))
    center = outline.getCenter()
    writting = Text(center, "Encode")
    outline.draw(win)
    writting.draw(win)

    # get input
    message_point = Point(1.8, 5)
    key_point = Point(1.8, 4)
    message_input = Entry(message_point, 20)
    key_input = Entry(key_point, 20)
    message_input.draw(win)
    key_input.draw(win)

    # close button
    win.getMouse()
    writting.undraw()
    outline.undraw()

    words = Text(Point(1.5, 2), "resulting message \n" +
                 code(message_input, key_input))
    words.draw(win)

    # leave
    leave = Text(Point(1.5, 1), "Click anywhere to close window")
    leave.draw(win)
    win.getMouse()
    win.close()


def main():
    draw()


if __name__ == "__main__":
    main()
