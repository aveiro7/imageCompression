def print_errors(original, transformed):
    result = []
    for i in range(len(original)):
        result.append(calculate_error(original[i], transformed[i]))
    print(result)


def print_errors2(original, transformed):
    for i in range(len(original)):
        result = []
        for j in range(len(original[i])):
            result.append(calculate_error(original[i][j], transformed[i][j]))
        print(result)


def calculate_error(rgb1, rgb2):
    r_diff = rgb1[0] - rgb2[0]
    g_diff = rgb1[1] - rgb2[2]
    b_diff = rgb1[2] - rgb2[2]

    return (r_diff**2 + g_diff**2 + b_diff**2)**(1.0 / 3.0)


def find_max_error(original, transformed):
    result = 0
    for i in range(len(original)):
        result = max(result, (calculate_error(original[i], transformed[i])))
    return result


def find_max_error2(original, transformed):
    result = 0
    for i in range(len(original)):
        for j in range(len(original[i])):
            result = max(result, (calculate_error(original[i][j], transformed[i][j])))
    return result


def count_pixels_with_difference(original, transformed):
    result = 0
    for i in range(len(original)):
        if calculate_error(original[i], transformed[i]) > 0:
            result += 1
    return result


def count_pixels_with_difference2(original, transformed):
    result = 0
    for i in range(len(original)):
        for j in range(len(original[i])):
            if calculate_error(original[i][j], transformed[i][j]) > 0:
                result += 1
    return result