import numpy
import math
from rgb_to_numbers import rgb_to_numbers2, numbers_to_rgb2

rotation_matrix = [[1 / math.sqrt(2), -1 / math.sqrt(2)],
                   [1 / math.sqrt(2), 1 / math.sqrt(2)]]


def rotate_point(x, y, clockwise=True):
    if clockwise:
        result = numpy.dot([x, y], rotation_matrix)
    else:
        result = numpy.dot([x, y], numpy.transpose(rotation_matrix))
    result_x = result[0]
    result_y = result[1]
    return result_x, result_y


def rotate_row(row):
    result_x = []
    result_y = []
    for i in range(0, len(row) - 1, 2):
        new_x, new_y = rotate_point(row[i], row[i + 1])
        result_x.append(new_x)
        result_y.append(new_y)
    return result_x, result_y


def rotate(data):
    result_x = []
    result_y = []
    for i in range(len(data)):
        new_x, new_y = rotate_row(data[i])
        result_x.append(new_x)
        result_y.append(new_y)
    return result_x, result_y


def compress(data):
    result = []
    for i in range(len(data)):
        result.append([])
        for j in range(len(data[i])):
            result[i].append(int(data[i][j]))
    return result


def derotate(data_x, data_y):
    result = []
    for i in range(len(data_x)):
        result.append([])
        for j in range(len(data_x[i])):
            new_x, new_y = rotate_point(data_x[i][j], data_y[i][j], False)
            result[i].append(int(new_x))
            result[i].append(int(new_y))
    return result


def rotational_compression_grayscale(data):
    rotated_x, rotated_y = rotate(data)
    rotated_y = compress(rotated_y)
    result = derotate(rotated_x, rotated_y)
    return result


def rotational_compression(data):
    r, g, b = rgb_to_numbers2(data)
    red_x, red_y = rotate(r)
    green_x, green_y = rotate(g)
    blue_x, blue_y = rotate(b)
    red_y = compress(red_y)
    green_y = compress(green_y)
    blue_y = compress(blue_y)
    result_r = derotate(red_x, red_y)
    result_g = derotate(green_x, green_y)
    result_b = derotate(blue_x, blue_y)
    result = numbers_to_rgb2(result_r, result_g, result_b)
    return result