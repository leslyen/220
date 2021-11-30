from graphics import *
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


def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        middle_value = values[middle]
        if search_val < middle_value:
            high = middle - 1
        if search_val > middle_value:
            low = middle + 1
        if search_val == middle_value:
            return True
    return False


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


def selection_sort(values):
    num = len(values)
    for bottom in range(num - 1):
        low = bottom
        for i in range(bottom + 1, num):
            if values[i] < values[low]:
                low = i
        values[bottom], values[low] = values[low], values[bottom]
    print(values)


def calc_area(rect):
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    x_1 = point_1.getX()
    y_1 = point_1.getY()
    x_2 = point_2.getX()
    y_2 = point_2.getY()
    width = x_2 - x_1
    height = y_2 - y_1
    area = width * height
    return area


def rect_sort(rectangles):
    num = len(rectangles)
    for bottom in range(num - 1):
        low = bottom
        for i in range(bottom + 1, num):
            if rectangles[i] < rectangles[low]:
                low = i
        rectangles[bottom], rectangles[low] = rectangles[low], rectangles[bottom]
