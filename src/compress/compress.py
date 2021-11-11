from werkzeug.datastructures import FileStorage
from io import BytesIO
from PIL import Image

img_formats = {
    "image/jpeg": "JPEG",
    "image/png": "PNG",
    "image/gif": "GIF",
    "image/bmp": "BMP",
}

def compressImage(file: FileStorage) -> BytesIO :
    image = Image.open(file.stream)

    img_io = BytesIO()
    image.save(img_io, img_formats[file.mimetype].upper())
    img_io.seek(0)
    return img_io
