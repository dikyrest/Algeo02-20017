from werkzeug.datastructures import FileStorage
from io import BytesIO
import numpy as np
from PIL import Image

img_formats = {
    "image/jpeg": "JPEG",
    "image/png": "PNG",
    "image/gif": "GIF",
    "image/bmp": "BMP",
}

# MAIN FUNCTION
def compressImage(file: FileStorage, ratio: int) -> BytesIO :
    image = Image.open(file.stream)

    matriksMerah, matriksHijau, matriksBiru = imageRGB(image)

    has_alpha = image.mode == 'RGBA'
    imageWidth, imageHeight = image.size

    mr = imageHeight
    mc = imageWidth
    originalSize = mr * mc * 3

    # Menghitung ukuran gambar setelah kompresi
    compressedSize = int ((100 - ratio) / 100 * originalSize)

    # Menghitung jumlah nilai singular yang dapat digunakan
    singularValuesLimit = int (compressedSize / (3 * (1 + mr + mc)))

    aRedCompressed = compressSingleChannel(matriksMerah, singularValuesLimit)
    aGreenCompressed = compressSingleChannel(matriksHijau, singularValuesLimit)
    aBlueCompressed = compressSingleChannel(matriksBiru, singularValuesLimit)

    imr = Image.fromarray(aRedCompressed, mode=None)
    img = Image.fromarray(aGreenCompressed, mode=None)
    imb = Image.fromarray(aBlueCompressed, mode=None)

    # Membuat matriks RGB
    newImage = Image.merge("RGB", (imr, img, imb))

    img_io = BytesIO()
    newImage.save(img_io, img_formats[file.mimetype].upper())
    img_io.seek(0)
    return img_io

# MATH FUNCTIONS
# Mengembalikan nilai eigen dan vektor eigen dari sebuah matriks
def find_eig(A):
    pQ = np.eye(A.shape[0])
    X = A.copy()
    for i in range(100):
        Q,R = np.linalg.qr(X)
        pQ = np.dot(pQ,Q)
        X = np.dot(R, Q)

    return np.diag(X), pQ

# Algoritma SVD menghasilkan matriks U, sigma, dan Vt
def svd(A):
    At = np.transpose(A)
    AAt = np.dot(A, At)
    lval, lvec = find_eig(AAt)

    AtA = np.dot(At, A)
    rval, rvec = find_eig(AtA)

    sigma = np.sqrt(rval)

    return lvec, sigma, rvec.T

# IMAGE FUNCTIONS
# Mengubah gambar menjadi matriks RGB
def imageRGB(image: Image):
    imageMatriks = np.array(image).astype(float)
    return imageMatriks[:, :, 0], imageMatriks[:, :, 1], imageMatriks[:, :, 2]

# Kompresi gambar dengan single channel
def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = svd(channelDataMatrix)
    aChannelCompressed = np.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
    k = singularValuesLimit

    leftSide = np.matmul(uChannel[:, 0:k], np.diag(sChannel)[0:k, 0:k])
    aChannelCompressedInner = np.matmul(leftSide, vhChannel[0:k, :])
    aChannelCompressed = aChannelCompressedInner.astype('uint8')
    return aChannelCompressed
