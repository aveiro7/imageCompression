import Image
from image_printer import save_image, print_image, print_grayscale_image


def get_luminance_chrominance(data):
    y = []
    u = []
    v = []
    for i in range(len(data)):
        y.append([])
        u.append([])
        v.append([])
        for j in range(len(data[i])):
            r = data[i][j][0]
            g = data[i][j][1]
            b = data[i][j][2]
            new_y = r * 0.299 + g * 0.587 + b * 0.114
            y[i].append(new_y)
            u[i].append((b - new_y) * 0.492)
            v[i].append((r - new_y) * 0.877)
    return y, u, v


def read_image(name):
    img = Image.open(name)
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
    return pixels


def convert_rgb_yuv(name):
    img = read_image(name)
    y, u, v = get_luminance_chrominance(img)
    print_grayscale_image(y)
    print_image(u)
    print_image(v)


convert_rgb_yuv("../../../Pictures/cookies.png")