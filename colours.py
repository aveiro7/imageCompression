import random


class Colour:
    # red colours
    light_coral = (240, 128, 128)
    salmon = (250, 128, 114)
    black = (0, 0, 0)
    crimson = (220, 20, 60)
    red = (255, 0, 0)

    # pink colours
    pink = (255, 192, 203)
    hot_pink = (255, 105, 180)
    deep_pink = (255, 105, 180)
    pale_violet_red = (219, 112, 147)

    # orange colours
    light_salmon = (255, 160, 122)
    tomato = (255, 99, 71)
    dark_orange = (255, 140, 0)
    orange = (255, 165, 0)

    # yellow colours
    yellow = (255, 255, 0)
    gold = (255, 215, 0)
    pale_goldenrod = (238, 232, 170)
    khaki = (240, 230, 140)

    # purple colours
    lavender = (230, 230, 250)
    orchid = (218, 112, 214)
    magenta = (255, 0, 255)
    blue_violet = (138, 43, 226)
    purple = (128, 0, 128)
    slate_blue = (106, 90, 205)

    # green colours
    green = (0, 255, 0)
    green_yellow = (173, 255, 47)
    lime_green = (50, 205, 50)
    light_green = (144, 238, 144)
    yellow_green = (154, 205, 50)
    olive = (128, 128, 0)
    teal = (0, 128, 128)

    # blue colours
    blue = (0, 0, 255)
    turqouise = (64, 224, 208)
    steel_blue = (70, 130, 180)
    deep_sky_blue = (0, 191, 255)
    cornflower_blue = (100, 149, 237)
    dark_blue = (25, 25, 112)

    # brown colours
    wheat = (245, 222, 179)
    tan = (210, 180, 140)
    goldenrod = (218, 165, 32)
    peru = (205, 133, 63)
    chocolate = (139, 69, 19)
    maroon = (128, 0, 0)
    brown = (153, 76, 0)

    # white colours
    white = (255, 255, 255)
    snow = (255, 250, 250)
    seashell = (255, 245, 238)
    beige = (245, 245, 220)
    ivory = (255, 255, 240)
    linen = (250, 240, 230)

    @staticmethod
    def generate_gray(value=0):
        if value == 0:
            value = random.randint(0, 255)
        return value, value, value
