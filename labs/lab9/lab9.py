"""
Name: Lesly Endara
lab9.py
certification of Authenticity:
I certify that this is entirely my own work
"""


def addTen(nums):
    new_list = []
    for parts in range(len(nums)):
        new_num = nums[parts] + 10
        new_list.append(new_num)


def squareEach(nums):
    for parts in range(len(nums)):
        new_num = nums[parts] ** 2
        nums[parts] = new_num


def sumList(nums):
    new_num = 0
    for parts in range(len(nums)):
        new_num = nums[parts] + new_num
    return new_num


def toNumbers(strList):
    for parts in range(len(strList)):
        real_num = eval(strList[parts])
        strList[parts] = real_num


def writeSumOfSquares():
    file_name = input("what is the name of the file, remember the file must have "
                      "at least two numbers on each line")
    file = open(file_name, "r")
    out_file = open("sum.txt", "w")
    lines = file.readlines()
    for things in lines:
        rid = things.replace('\n', '')
        nums = rid.split(' ')
        toNumbers(nums)
        squareEach(nums)
        answer = sumList(nums)
        out_file.write("Sum of squares = " + str(answer) + '\n')

    file.close()
    out_file.close()


def leapYear(year):
    answer = ''
    if year % 400 == 0:
        answer = True
        answer = 'is a leap year'
    elif not(year % 100 == 0) and year % 4 == 0:
        answer = True
        answer = 'is a leap year'
    else:
        answer = False
        answer = 'is not a leap year'
    print(year, answer)


def main():
    #addTen()
    #squareEach()
    #sumList()
    #toNumbers()
    #writeSumOfSquares()
    leapYear(2012)

    pass


main()
