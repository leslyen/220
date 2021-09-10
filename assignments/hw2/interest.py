"""
Name: Lesly Endara
interest.py

Problem: find the monthly interest rate of a credit card


certification of Authenticity:
I certify that this is entirely my own work
"""


def main():
    interest_rate = eval(input("please input your annual interest rate:"))
    number_of_days = eval(input("how many days is there in your billing cycle?: "))
    balance = eval(input("please input your balance number:"))
    calc_one = balance * 31
    net = eval(input("please input how much you've paid for your balance:"))
    cycle = eval(input("how many days into your cycle has it been?:"))
    month_count = number_of_days - cycle
    calc_two = net * month_count
    calc_three = calc_one - calc_two
    daily = calc_three / number_of_days
    percentage = (interest_rate / 12) / 100
    monthly_interest = daily * percentage
    print("your monthly interest rate is", monthly_interest)



if __name__ == "__main__":
    main()