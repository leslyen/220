"""
Name: Lesly Endara
lab3.py
problem: using arithmetic and loops to solve problems

certification of Authenticity:
I certify that this is entirely my own work, worked with Jessica, Katie
"""

def average():
    number_of_grades = eval(input("How many grades will you input?: "))
    homework_sum = 0
    for times in range(number_of_grades):
        homework_grade = eval(input("Enter your grade on HW" + str(times + 1)))
        homework_sum = homework_grade + homework_sum
    homework_total = homework_sum / number_of_grades
    print(homework_total)


def tip_jar():
    sum_of_tips = 0
    for tips in range(5):
        amount = eval(input("how much will you be donating today?: "))
        sum_of_tips = amount + sum_of_tips
        # end for loop
    print("We raised", sum_of_tips)


def newton():
    x = eval(input("what will be x: "))
    approx = eval(input("what will be the number of approximation?: "))
    for number in range(approx):
        approx = (approx + (x / approx)) / 2
        # end for loop
    print("x was", x, "and your approx will be", approx)


def sequence():
    series = eval(input("please input the number of terms in a series"))
    starter = 1
    for seq in range(0, series):
        remainder = seq % 2
        starter = starter + (remainder * 2)
        print(starter, end="")
        # end for loop


def pi():
    series = eval(input("input a number for n: "))
    even = 2
    odd = 1
    for seq in range(0, series):
        remainder = seq % 2
        odd_remainder = seq % 1
        even = even + (remainder * 2)
        odd = odd + (remainder * 2)
        print(even, end="")
        # end for loop
        # tried, will keep trying later.
