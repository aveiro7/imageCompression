import random


class Colour:
    light_coral = (240, 128, 128)
    salmon = (250, 128, 114)
    black = (0, 0, 0)
    crimson = (220, 20, 60)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    pink = (255, 192, 203)
    hot_pink = (255, 105, 180)
    deep_pink = (255, 105, 180)
    pale_violet_red = (219, 112, 147)


    @staticmethod
    def generate_gray(value=0):
        if value == 0:
            value = random.randint(0, 255)
        return (value, value, value)
