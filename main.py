# import modules
import qrcode
import argparse
import numpy as np
from PIL import Image, ImageDraw

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outputFilename', default='output.png', required=False,
                        help="Output filename, eg: output.png")
    parser.add_argument('-qc', '--qrColor', default='BLACK', required=False,
                        help="Color of the generated qr-code. eg: #314a4e")
    parser.add_argument('-qb', '--qrBackgroundColor', default='WHITE', required=False,
                        help="Color of the generated qr-code, eg: #ffffff")
    parser.add_argument('-qs', '--qrSize', type=int, default=3000, required=False,
                        help="qr-code size in pixels, eg: '3000'")
    parser.add_argument('-l', '--logoAddition', default='logo.png', required=False,
                        help="filename of log for addition, eg: logo.png")
    parser.add_argument('-ls', '--logoSizeRatio', type=float, default=0.25, required=False,
                        help="size ratio of logo compared to qr-code, eg: '0.25' (for 25 percent of qr code)")
    parser.add_argument('-lc', '--logoCircleShape', action='store_true', required=False,
                        help="create logo as circle")
    parser.add_argument('content')
    parsed = parser.parse_args()
    print('Input:', vars(parsed))
    return parsed


def create_logo(filename_of_logo, qr_size, logo_size_ratio=0.25, background_color=None):
    if arguments.logoCircleShape:
        origin = Image.open(filename_of_logo).convert("RGB")
        origin = create_circle(origin)
    else:
        origin = Image.open(filename_of_logo).convert("RGBA")

    image = Image.new("RGB", origin.size, background_color)
    image.paste(origin, mask=origin)

    # adjust image size
    logoWidth = int(qr_size * logo_size_ratio)
    resizeRatio = (logoWidth / float(image.size[0]))
    logoHeight = int((float(image.size[1]) * float(resizeRatio)))
    return image.resize((logoWidth, logoHeight), Image.LANCZOS)


def create_circle(img):
    npImage = np.array(img)
    h, w = img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)

    # Convert alpha Image to numpy array
    npAlpha = np.array(alpha)

    # Add alpha layer to RGB
    npImage = np.dstack((npImage, npAlpha))

    return Image.fromarray(npImage)


if __name__ == '__main__':
    arguments = main()

    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    # adding URL or text to QRcode
    QRcode.add_data(arguments.content)
    QRcode.make()
    img = QRcode.make_image(
        fill_color=arguments.qrColor, back_color=arguments.qrBackgroundColor).convert('RGB')
    img = img.resize((arguments.qrSize, arguments.qrSize), Image.NEAREST)

    if arguments.logoAddition:
        logo = create_logo(arguments.logoAddition, arguments.qrSize, logo_size_ratio=arguments.logoSizeRatio,
                           background_color=arguments.qrBackgroundColor)
        # set size of QR code
        pos = ((img.size[0] - logo.size[0]) // 2,
               (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)

    # save the QR code generated
    img.save(arguments.outputFilename)

    print('QR code generated with filename: ' + arguments.outputFilename + '!')