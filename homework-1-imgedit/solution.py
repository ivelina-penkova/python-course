def rotate_left(picture):
    return [list(x) for x in zip(*picture)][::-1]


def rotate_right(picture):
    return [list(x) for x in zip(*picture[::-1])]


def invert_color(pixel):
    return(
        255 - pixel[0],
        255 - pixel[1],
        255 - pixel[2]
        )


def invert(picture):
    return [[invert_color(pixel) for pixel in row] for row in picture]


def lighten_single(color, factor):
    new = color + factor * (255 - color)
    if new > 255:
        return 255
    else:
        return int(new)


def lighten_pixel(pixel, factor):
    return (
        lighten_single(pixel[0], factor),
        lighten_single(pixel[1], factor),
        lighten_single(pixel[2], factor)
        )


def darken_pixel(pixel, factor):
    return (
        int(pixel[0] * (1 - factor)),
        int(pixel[1] * (1 - factor)),
        int(pixel[2] * (1 - factor))
        )


def lighten(picture, factor):
    return [[lighten_pixel(pixel, factor) for pixel in row] for row in picture]


def darken(picture, factor):
    return [[darken_pixel(pixel, factor) for pixel in row] for row in picture]


def partial_histogram(picture, i):
    partial = {}
    for row in picture:
        for pixel in row:
            if pixel[i] in partial:
                partial[pixel[i]] = partial[pixel[i]] + 1
            else:
                partial[pixel[i]] = 1
    return partial


def create_histogram(picture):
    return {
        'red': partial_histogram(picture, 0),
        'green': partial_histogram(picture, 1),
        'blue': partial_histogram(picture, 2)
        }
