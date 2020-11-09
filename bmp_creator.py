from struct import pack


def header(width, height):
    file_type = 19778
    res_1 = 0
    res_2 = 0
    pix_offset = 62
    file_size = pix_offset + 1 * width * height
    return pack('<HLHHL', file_type, file_size, res_1, res_2, pix_offset)


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
    total_colors = 0
    major_colors = 0
    return pack('<LLLHHLLLLLL', header_size,
                image_width, image_height,
                planes, pix_bits,
                compression, image_size,
                x_pix, y_pix,
                total_colors, major_colors)


def color():
    color_1 = (0, 0, 0, 0)
    color_2 = (255, 255, 255, 0)
    return pack('<BBBBBBBB', *color_1, *color_2)


def pixel_data(pixels):
    pix_data = b''
    for px in reversed(pixels):
        pix_data += pack('<B', px)
    return pix_data


def create_bmp(file_name, pixels, width, height):
    with open(file_name, 'wb') as f:
        f.write(header(width, height))
        f.write(info(width, height))
        f.write(color())
        f.write(pixel_data(pixels))


if __name__ == "__main__":
    width = 4
    height = 4
    pix = [0, 1, 1, 0,
           1, 0, 0, 1,
           1, 1, 1, 1,
           1, 0, 0, 1]
    create_bmp('test.bmp', pix, 4, 4)
