from PIL import Image


def decipher(png_path) -> str:
    """
    :param png_path: path of the cipher file
    :return: return the hidden message
    """
    image = Image.open(png_path)
    width, height = image.size[0], image.size[1]
    # 1 is black color
    secret_msg = list(map(lambda x: chr(x), [h for w in range(width) for h in range(height) if image.getpixel((w, h)) ==
                                             1]))
    return ''.join(secret_msg)


if __name__ == '__main__':
    print(decipher(r'C:\Users\noase\Downloads\code.png'))

