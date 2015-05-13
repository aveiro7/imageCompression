from image_printer import generate_squares, print_image
from colours import Colour as c


begin_data = [[c.hot_pink, c.crimson, c.salmon],
              [c.crimson, c.salmon, c.hot_pink],
              [c.salmon, c.hot_pink, c.crimson]]
squared_data = generate_squares(begin_data)
print_image(squared_data)