from simple_rotation import rotational_compression_grayscale
from haar import haar_compression_grayscale, haar_compression
from image_printer import save_grayscale_image, generate_squares, save_image
from image_printer import print_image, print_grayscale_image
from error_rate import find_max_error2, count_pixels_with_difference2
from dct import cosine_compression_grayscale

continuous_tone_pattern = [[0, 10, 20, 30, 30, 20, 10, 0],
                           [10, 20, 30, 40, 40, 30, 20, 10],
                           [20, 30, 40, 50, 50, 40, 30, 20],
                           [30, 40, 50, 60, 60, 50, 40, 30],
                           [30, 40, 50, 60, 60, 50, 40, 30],
                           [20, 30, 40, 50, 50, 40, 30, 20],
                           [10, 20, 30, 40, 40, 30, 20, 10],
                           [0, 10, 20, 30, 30, 20, 10, 0]]


discrete_tone_image = [[0, 200, 0, 0, 0, 0, 0, 200],
                       [0, 0, 200, 0, 0, 0, 200, 0],
                       [0, 0, 0, 200, 0, 200, 0, 0],
                       [0, 0, 0, 0, 200, 0, 0, 0],
                       [0, 0, 0, 0, 200, 0, 0, 0],
                       [0, 0, 0, 0, 200, 0, 0, 0],
                       [0, 0, 0, 0, 200, 0, 0, 0],
                       [0, 0, 0, 0, 200, 0, 0, 0]]

dct_pattern = [[100, 0, 0, 100, 100, 100, 0, 1],
               [100, 100, 0, 0, 100, 0, 100, 100],
               [0, 100, 100, 0, 0, 100, 0, 0],
               [0, 0, 0, 100, 0, 0, 100, 0],
               [0, 100, 0, 0, 100, 0, 100, 100],
               [100, 100, 100, 0, 0, 100, 100, 0],
               [100, 100, 0, 0, 100, 0, 100, 100],
               [0, 100, 0, 100, 0, 0, 100, 0]]

stripes = [[0, 200, 0, 200, 0, 200, 0, 200],
           [0, 200, 0, 200, 0, 200, 0, 200],
           [0, 200, 0, 200, 0, 200, 0, 200],
           [0, 200, 0, 200, 0, 200, 0, 200],
           [0, 200, 0, 200, 0, 200, 0, 200],
           [0, 200, 0, 200, 0, 200, 0, 200],
           [0, 200, 0, 200, 0, 200, 0, 200],
           [0, 200, 0, 200, 0, 200, 0, 200]]
