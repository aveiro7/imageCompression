from PIL import Image
from colours import Colour as c


square_size = 20


def print_image(data):
    height = len(data)
    width = len(data[0])
    img = Image.new('RGB', (height, width), "black")
    pixels = img.load()
    for i in range(0, height, 1):
        for j in range(0, width, 1):
            pixels[j, i] = data[i][j]
    img.show()


def generate_squares(data):
    result = []
    for i in range(len(data)):
        for l in range(square_size * i, square_size * i + square_size, 1):
            result.append([])
            for j in range(len(data[i])):
                for k in range(square_size * j, square_size * j + square_size, 1):
                    result[l].append(data[i][j])
    return result

def generate_gray_squares(size):
    result = [];
    for i in range(0, size, 1):
        result.append([])
        for j in range(0, size, 1):
            result[i].append(c.generate_gray())
    # result = generate_squares(result)
    return result