def read_data(filename):
    inside = open(filename, "r")
    parts = inside.read()
    numbers = parts.split()
    list = []
    i = 0
    while i < len(numbers):
        new_list = eval(numbers[i])
        list.append(new_list)
        i += 1
    inside.close()
    return list


def is_in_linear(search_val, values):
    i = 0
    answer = False
    try:
        while i < len(values):
            parts = values.index(search_val)
            if values[parts] == search_val:
                answer = True
            i += 1
    except:
        answer = False
    return answer