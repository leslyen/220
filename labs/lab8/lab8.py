"""
Name: Lesly Endara
lab8.py
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w')
    lines = infile.read()
    separate = lines.split()
    for parts in range(len(separate)):
        outfile.write(str(parts + 1) + ' ')
        outfile.write((separate[parts]))
        outfile.write('\n')
    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w')
    read_old_wage = infile.read()
    lines = read_old_wage.split('\n')
    for parts in range(len(lines)):
        old_wage = lines[parts].split()
        new_pay = eval(old_wage[2]) + 1.65
        outfile.write(str(old_wage[0]) + ' ' + str(old_wage[1]))
        outfile.write(' ' + str(new_pay) + '\n')
    outfile.close()
    infile.close()


def calc_check_sum(isbn):
    numbers = isbn.replace('', ' ')
    list = numbers.split(' ')
    times = 10
    total = 0
    for count in range(1, (len(list) - 1)):
        num = eval(list[count]) * times
        total = num + total
        times = times - 1
    return total


def send_message(file, friend):
    infile = open(file, 'r')
    reading = infile.read()
    new_name = str(friend + '.txt')
    outfile = open(new_name, 'w')
    outfile.write(reading)
    infile.close()
    outfile.close()
    return


def send_safe_message(file, friend, key):
    infile = open(file, 'r')
    reading = infile.read()
    new_name = str(friend + '.txt')
    outfile = open(new_name, 'w')
    outfile.write(encode(reading, key))
    infile.close()
    outfile.close()
    return


# def send_uncrackable_message(file, friend, pad):


def main():
    number_words("Walrus.txt", "result.txt")
    hourly_wages("hourly_wages.txt", "new_pay.txt")
    calc_check_sum('0072946520')
    send_message("message.txt", "Shyann")
    send_safe_message("secret_message.txt", "Katrina", 3)
    # send_uncrackable_message("safest_message.txt", "Jane" , "pad.txt")
    pass


main()
