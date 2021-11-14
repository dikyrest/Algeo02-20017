from werkzeug.datastructures import FileStorage
from io import BytesIO
from PIL import Image
import numpy as np

img_formats = {
    "image/jpeg": "JPEG",
    "image/png": "PNG",
    "image/gif": "GIF",
    "image/bmp": "BMP",
}

def compressImage(file: FileStorage, ratio: int) -> BytesIO :
    image = Image.open(file.stream)

    has_alpha = image.mode == 'RGBA'
    imageWidth, imageHeight = image.size

    nImage = np.array(image)
    r = nImage[:, :, 0]
    g = nImage[:, :, 1]
    b = nImage[:, :, 2]

    mr = imageHeight
    mc = imageWidth
    originalSize = mr * mc * 3

    # Menghitung ukuran gambar setelah kompresi
    compressedSize = int ((100 - ratio) / 100 * originalSize)

    # Menghitung jumlah nilai singular yang dapat digunakan
    singularValuesLimit = int (compressedSize / (3 * (1 + mr + mc)))

    aRedCompressed = compressSingleChannel(r, singularValuesLimit)
    aGreenCompressed = compressSingleChannel(g, singularValuesLimit)
    aBlueCompressed = compressSingleChannel(b, singularValuesLimit)

    imr = Image.fromarray(aRedCompressed, mode=None)
    img = Image.fromarray(aGreenCompressed, mode=None)
    imb = Image.fromarray(aBlueCompressed, mode=None)

    # Membuat matriks RGB
    newImage = Image.merge("RGB", (imr, img, imb))

    img_io = BytesIO()
    newImage.save(img_io, img_formats[file.mimetype].upper())
    img_io.seek(0)
    return img_io

# FUNCTION DEFINTIONS:

# Kompresi gambar dengan single channel
def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = np.linalg.svd(channelDataMatrix) #jabarin SVD nya
    aChannelCompressed = np.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
    k = singularValuesLimit

    leftSide = np.matmul(uChannel[:, 0:k], np.diag(sChannel)[0:k, 0:k])
    aChannelCompressedInner = np.matmul(leftSide, vhChannel[0:k, :])
    aChannelCompressed = aChannelCompressedInner.astype('uint8')
    return aChannelCompressed
