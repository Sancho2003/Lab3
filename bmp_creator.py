from struct import pack


def header(height, width):
    file_type = 19778
    res_1 = 0
    res_2 = 0
    pix_off = 62
    file_size = pix_off + 1 * height * width
    return pack('<HLHHL', file_type, file_size, res_1, res_2, pix_off)


def info(height, width):
    header_size = 60
    image_height = height
    image_width = width
    plane = 1
    image_size = 0
    compression = 0
    pix_x = 0
    pix_y = 0
    general_colors = 0
    major_colors = 0
    pix_bit = 8
    return pack('<LLLHLLLLLLH', header_size,
                image_height, image_width,
                plane, image_size,
                compression, pix_x, pix_y,
                general_colors, major_colors, pix_bit)


def pixel_data(pixels):
    pix_data = b''
    for pix in reversed(pixels):
        pix_data += pack('<B', pix)
    return pix_data


def color():
    color_1 = (0, 0, 0, 0)
    color_2 = (255, 255, 255, 0)
    return pack('<BBBBBBBB', *color_1, *color_2)


def create_bmp(name, pixels, height, width):
    with open(name, 'wb') as f:
        f.write(header(height, width))
        f.write(info(height, width))
        f.write(color())
        f.write(pixel_data(pixels))


if __name__ == '__main__':
    height = 4
    width = 4
    pixel = [0, 1, 1, 0,
             1, 0, 0, 1,
             1, 1, 1, 1,
             1, 0, 0, 1]
    create_bmp('test.bmp', pixel, 4, 4)
