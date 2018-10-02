import base64
from io import BytesIO

import numpy
from PIL import Image, ImageDraw


def crop_image(base64_image, coordinates):

    decoded_image = Image.open(BytesIO(base64.b64decode(base64_image))).convert("RGBA")

    image_array = numpy.asarray(decoded_image)

    mask = Image.new('L', (image_array.shape[1], image_array.shape[0]), 0)
    ImageDraw.Draw(mask).polygon(coordinates, outline=1, fill=1)
    mask = numpy.array(mask)

    cropped_image_array = numpy.empty(image_array.shape, dtype='uint8')
    cropped_image_array[:, :, :3] = image_array[:, :, :3]
    cropped_image_array[:, :, 3] = mask * 255

    cropped_image = Image.fromarray(cropped_image_array, "RGBA")
    # Could've used named temporary file here. Skipping for  now.
    cropped_image.save("temporary_file.png")

    with open("temporary_file.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string
