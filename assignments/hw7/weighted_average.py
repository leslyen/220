"""
Name: Lesly Endara
weighted_average.py

read grades from grades.txt file and get their average.

certification of Authenticity:
I certify that this is entirely my own work
"""


def weighted_average(in_file_name, out_file_name):
    grades_file = open(in_file_name, 'r')
    average_file = open(out_file_name, 'w')
    info = grades_file.read()
    total_average = []
    new_line = info.split('\n')

    for inside in range(len(new_line)):
        word_separate = new_line[inside].split(': ')
        separate = word_separate[1].split()
        grades, weight = [], []
        add = 0
        result_average = ""

        for count in range(0, len(separate), 2):
            weight_list = eval(separate[count])
            weight.append(weight_list)

        for count in range(1, len(separate), 2):
            grades_list = eval(separate[count])
            grades.append(grades_list)

        for count in range(len(grades)):
            multiplied = (weight[count]) * (grades[count])
            add = multiplied + add
            divided = add / 100
            total_average.append(divided)
            result_average = str(round(divided, 1))

        if sum(weight) == 100:
            average_file.write(word_separate[0] + "'s average: " + result_average + '\n')

        elif sum(weight) < 100:
            average_file.write(word_separate[0] + "'s average: Error: The weights are less than 100." + '\n')

        elif sum(weight) > 100:
            average_file.write(word_separate[0] + "'s average: Error: The weights are more than 100." + '\n')

    class_average = (sum(total_average) / len(total_average))
    average_file.write("Class average: " + str(round(class_average, 1)))

    grades_file.close()
    average_file.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
