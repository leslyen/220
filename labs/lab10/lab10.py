"""
create a tic-tac-toe game
Name: Lesly Endara
lab10.py
certification of Authenticity:
I certify that this is entirely my own work
"""
import time


def start_board():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return nums


def draw_board(nums):
    list_num = nums
    print("tic-tac-toe")
    print(list_num[0] + '|', list_num[1], '|', list_num[2])
    print("_________")
    print(list_num[3] + '|', list_num[4], '|', list_num[5])
    print("_________")
    print(list_num[6] + '|', list_num[7], '|', list_num[8])


def change(board, position, character):
    character = character.upper()
    if character == 'X' or character == 'O':
        board[position - 1] = character
        draw_board(board)
    else:
        return "stop"

def validation(var):
    num = str(var).isnumeric()
    if num:
        return True
    else:
        return False


def win(lines):
    if lines[0] == lines[1] == lines[2]:
        return True
    elif lines[3] == lines[4] == lines[5]:
        return True
    elif lines[6] == lines[7] == lines[8]:
        return True
    elif lines[0] == lines[3] == lines[6]:
        return True
    elif lines[1] == lines[4] == lines[7]:
        return True
    elif lines[2] == lines[5] == lines[8]:
        return True
    elif lines[0] == lines[4] == lines[8]:
        return True
    elif lines[2] == lines[4] == lines[6]:
        return True
    else:
        return False


def main():
    # add other function calls here
    print("Hello, welcome to Squid Games, if you loose you will be eliminated")
    print("Here are the rules:")
    print("you have to put in a number from 1-9 and either an x or an o")
    time.sleep(6)
    print("this game will only work if you space out the number and the letter")
    time.sleep(5)
    print("let the game begin")
    thing = 6
    for i in range(5):
        thing = thing - 1
        print(thing)
        time.sleep(1)
    parts = start_board()
    draw_board(parts)
    for i in range(len(parts)):
        if win(parts) is False:
            answer = input("what is the position and character?")
            answer = answer.split(" ")
            number = int(answer[0])
            character = answer[1]
            if validation(parts[number - 1]) is True:
                change(parts, number, character)
            else:
                print("try again")
        else:
            character = character.upper()
            print("player", character, "wins")
            break
    pass


main()
