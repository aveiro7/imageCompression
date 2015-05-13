from rgb_to_numbers import rgb_to_numbers2, numbers_to_rgb2
from scipy.fftpack import dct, idct


def transform(data):
    result = []
    for i in range(len(data[0])):
        result.append([])

    for i in range(len(data)):
        partial_result = dct(data[i])
        for j in range(len(partial_result)):
            result[j].append(partial_result[j])

    final_result = []
    for i in range(len(result)):
        partial_result = dct(result[i])
        final_result.append(partial_result)
    return final_result


def inverse_transform(data):
    result = []
    for i in range(len(data[0])):
        result.append([])

    for i in range(len(data)):
        partial_result = idct(data[i])
        for j in range(len(partial_result)):
            result[j].append(partial_result[j])

    final_result = []
    for i in range(len(result)):
        partial_result = idct(result[i])
        final_result.append(partial_result)
    return final_result


def compress(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    convert_to_real(data)
    return data


def convert_to_real(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
    return data


def cosine_compression(data):
    r, g, b = rgb_to_numbers2(data)
    r = convert_to_real(r)
    g = convert_to_real(g)
    b = convert_to_real(b)
    t_r = transform(r)
    t_g = transform(g)
    t_b = transform(b)
    t_r = compress(t_r)
    t_g = compress(t_g)
    t_b = compress(t_b)
    ir = inverse_transform(t_r)
    ig = inverse_transform(t_g)
    ib = inverse_transform(t_b)

    result = numbers_to_rgb2(ir, ig, ib)
    return result


def cosine_compression_grayscale(data):
    data = convert_to_real(data)
    transformed_data = transform(data)
    transformed_data = compress(transformed_data)
    result = inverse_transform(transformed_data)
    return result