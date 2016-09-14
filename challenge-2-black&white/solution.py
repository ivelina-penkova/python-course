def grey(pixel): return ((int(sum(pixel) / 3)),) * 3


def grayscale(func):
    def wrapper_func(image, *args):
        new_image = [[grey(pixel) for pixel in row] for row in image]
        return func(new_image, *args)
    return wrapper_func