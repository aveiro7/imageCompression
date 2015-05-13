import pywt
from rgb_to_numbers import rgb_to_numbers2, numbers_to_rgb2


def calculate_coefficients(data):
    red, green, blue = rgb_to_numbers2(data)
    result_red = pywt.dwt2(red, "haar")
    result_green = pywt.dwt2(green, "haar")
    result_blue = pywt.dwt2(blue, "haar")

    return result_red, result_green, result_blue


def calculate_coefficients_gray(data):
    return pywt.dwt2(data, "haar")


def image_from_coefficients(red, green, blue):

    result_red = pywt.idwt2(red, "haar")
    result_green = pywt.idwt2(green, "haar")
    result_blue = pywt.idwt2(blue, "haar")

    result = numbers_to_rgb2(result_red, result_green, result_blue)
    return result


def image_from_coefficients_gray(data):
    result = pywt.idwt2(data, "haar")
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] = int(result[i][j])
    return result


def compress(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    return data


def haar_compression(data):
    r, g, b = calculate_coefficients(data)
    r = compress(r)
    g = compress(g)
    b = compress(b)

    result = image_from_coefficients(r, g, b)
    return result


def haar_compression_grayscale(data):
    cA, (cH, cV, cD) = calculate_coefficients_gray(data)
    cA = compress(cA)
    cH = compress(cH)
    cD = compress(cD)

    coefficients = cA, (cH, cV, cD)
    result = image_from_coefficients_gray(coefficients)
    return result