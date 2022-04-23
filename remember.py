from PIL import Image


def decipher(png_path):
    """
    :param png_path: path of the cipher file
    :return: return the hidden message
    """
    img = Image.open(png_path)
    img = img.convert('RGB')
    width, height = img.size[0], img.size[1]
    secret_msg = ''
    for w in range(width):
        for h in range(height):
            # (1,1,1) dark color  in rgb
            if img.getpixel((w, h)) == (1, 1, 1):
                secret_msg += chr(h)
    return secret_msg


if __name__ == '__main__':
    print(decipher(r'C:\Users\noase\Downloads\code.png'))


