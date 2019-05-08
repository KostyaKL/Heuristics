import numpy as np
import math


def exercise1(string):
    print(len(string))
    return string.upper()


def exercise2(char, string):
    if char in string:
        return 1
    return 0


def exercise3(string, substring):
    if substring in string:
        return True
    return False


def exercise4(string):
    result = ""
    for c in string:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    return result


def exercise5(lines, columns):
    half = lines/2
    for i in range(lines):
        if i < half:
            for j in range(columns):
                print("*", end="")
        else:
            for j in range(columns):
                print("+", end="")
        print("\n")


def exercise6(char, rows, columns):
    inner_list = [char] * columns
    list_of_inner_lists = [inner_list] * rows
    return list_of_inner_lists

def exercise7(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    if x < 0 or y < 0:
        print("X and Y cannot be negative!")
    else:
        m = np.matrix([[1, 2, 3, 4],
                       [4, 5, 6, 7],
                       [8, 9, 10, 11]])
        rows = m.shape[0]
        columns = m.shape[1]
        neighbors = []
        if (y - 1) >= 0:
            neighbors.insert(0, (x, y - 1))
        if (y + 1) < columns:
            neighbors.insert(1, (x, y + 1))
        if (x - 1) >= 0:
            neighbors.insert(2, (x - 1, y))
        if (x + 1) < rows:
            neighbors.insert(3, (x + 1, y))
        return neighbors


def exercise8(rows, columns, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    if x < 0 or y < 0:
        print("X and Y cannot be negative!")
    else:
        if x >= rows or y >= columns:
            print("Out of map's bound")
        else:
            neighbors = []
            if (y - 1) >= 0:
                neighbors.insert(0, (x, y - 1))
            if (y + 1) < columns:
                neighbors.insert(1, (x, y + 1))
            if (x - 1) >= 0:
                neighbors.insert(2, (x - 1, y))
            if (x + 1) < rows:
                neighbors.insert(3, (x + 1, y))
            return neighbors


def exercise9(string, coordinate1, coordinate2):
    x1 = coordinate1[0]
    y1 = coordinate1[1]
    x2 = coordinate2[0]
    y2 = coordinate2[1]
    if string == "euclidean":
        return math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
    else:
        if string == "manhattan":
            return math.fabs(x1-x2) + math.fabs(y1-y2)

# print(exercise1("aaAaa"))
# print(exercise2('b', "aaa"))
# print(exercise3('abcabc', 'abc'))
# print(exercise4("aAa"))
# exercise5(4, 5)
# print(exercise6("t", 3, 4))
# print(exercise7((2, 3)))
# print(exercise8(3, 4, (2, 3)))
# print(exercise9("manhattan", (1, 2), (3, 5)))
