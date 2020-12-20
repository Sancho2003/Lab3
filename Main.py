from struct import pack
from math import sin, cos, pi


def pixels_creating(start, stop, step):
    pixels = []
    min_x = min_y = float('inf')
    t = start
    while t <= stop:
        x = round(16*(sin(3*t)**3), 2)
        if x < min_x:
            min_x = x
        y = round(13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t), 2)
        if y < min_y:
            min_y = y
        pixels.append((x, y))
        t += step
    pixels.reverse()
    return pixels, min_x, min_y


def header(width, height):
    file_type = 19778
    res_1 = 0
    res_2 = 0
    pix_offset = 62
    file_size = pix_offset + 1 * width * height
    return pack('<HL2HL', file_type, file_size, res_1, res_2, pix_offset)


def info(width, height):
    header_size = 40
    image_width = width
    image_height = height
    planes = 1
    pix_bits = 8
    compression = 0
    image_size = 0
    x_pix = 0
    y_pix = 0
    total_colors = 2
    major_colors = 0
    return pack('<3L2H6L', header_size,
                image_width, image_height,
                planes, pix_bits,
                compression, image_size,
                x_pix, y_pix,
                total_colors, major_colors)


def color():
    color_1 = (0, 0, 0, 0)
    color_2 = (255, 255, 255, 0)
    return pack('<8B', *color_1, *color_2)


def result_writing(start, stop, step, height, width, filename):
    with open(f'{filename}.bmp', 'wb') as f:
        f.write(header(width, height))
        f.write(info(width, height))
        f.write(color())
        pixels, min_x, min_y = pixels_creating(start, stop, step)

        pix_y = min_y
        for i in range(height):
            pix_x = min_x
            for j in range(width):
                if (pix_y, pix_x) in pixels:
                    f.write(pack('<B', 0))
                else:
                    f.write(pack('<B', 1))
                pix_x = round(pix_x + step, 5)
            pix_y = round(pix_y + step, 5)


if __name__ == '__main__':
    result_writing(0, 2 * pi, 0.01, 600, 600, 'result')
