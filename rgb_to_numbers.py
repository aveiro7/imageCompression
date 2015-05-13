def rgb_to_numbers(data):
    red = []
    green = []
    blue = []
    print(data)
    for i in range(len(data)):
        red.append(data[i][0])
        green.append(data[i][1])
        blue.append(data[i][2])
    print(red)
    print("\n")
    print(green)
    print("\n")
    print(blue)
    return red, green, blue


def rgb_to_numbers2(data):
    red = []
    green = []
    blue = []
    for i in range(len(data)):
        red.append([])
        green.append([])
        blue.append([])

        for j in range(len(data[i])):
            red[i].append(data[i][j][0])
            green[i].append(data[i][j][1])
            blue[i].append(data[i][j][2])

    return red, green, blue


def numbers_to_rgb(red, green, blue):
    result = []
    for i in range(len(red)):
        rgb = tuple([red[i], green[i], blue[i]])
        result.append(rgb)
    print(result)
    return result


def numbers_to_rgb2(red, green, blue):
    result = []
    for i in range(len(red)):
        result.append([])
        for j in range(len(red[i])):
            rgb = tuple([int(red[i][j]), int(green[i][j]), int(blue[i][j])])
            result[i].append(rgb)
    return result

    return result

