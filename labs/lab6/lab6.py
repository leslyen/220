"""
Name: Lesly Endara

lab6.py

certification of Authenticity:
I certify that this is entirely my own work
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("what is your first and last name? ")
    order = name.split()
    print(order[1] + ", " + order[0])


def company_name():
    company = input("Please enter a company's name as a three-part internet domain")
    order = company.split(".")
    print(order[1])


def initials():
    amount = eval(input("How many students will you be registering? "))
    for repeat in range(amount):
        first_name = input("Enter the first name of student " + str(repeat + 1) + ": ")
        last_name = input("Enter the last name of student " + str(repeat + 1) + ":")
        print(first_name + "'s initials are " + first_name[0] + last_name[0])


def names():
    people = input("Enter people's names, separated by commas: ")
    different_names = people.split(",")
    next = 0

    print("The initials are", end=" ")
    for i in range(len(different_names)):
        separate_name = people.split(" ")
        first = separate_name[next]
        next += 1
        last = separate_name[next]
        print(first[0] + last[0], end=" ")
        next += 1


def thirds():
    amount = eval(input("How many sentences will you input? "))
    time = 0
    for number in range(amount):
        sentences = input("please input a sentence")
        for output in range(2, len(sentences), 3):
            #count = len(sentences)
            print(sentences[output], end="")
        print("")


def word_average():
    amount = eval(input("How many sentences will you input? "))
    time = 0
    count = 0
    for number in range(amount):
        sentences = input("please input a sentence")
        words = sentences.split()
        for output in range(len(words)):
            number = len(words)
            count = len(sentences[output]) + count
            average = count / number
        print(average)
        print("")


#def pig_latin():
    #words

def main():
    # name_reverse()
    # company_name()
    #initials()
    #names()
    #thirds()
    word_average()
    #pig_latin()
    # add other function calls here


main()
