import numpy as np
from PIL import Image

# FUNCTION DEFINTIONS:
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

    u = lvec
    sigma = np.sqrt(rval)
    vt = np.linalg.pinv(sigma)
    vt = np.dot(vt, np.linalg.pinv(u))
    vt = np.dot(vt, A)

    return u, sigma, vt

# Mengubah gambar menjadi matriks RGB
def openImage(imagePath):
    imageOrigin = Image.open(imagePath)
    imageMatriks = np.array(imageOrigin).astype(float)
    return imageMatriks[:, :, 0], imageMatriks[:, :, 1], imageMatriks[:, :, 2], imageOrigin

# Kompresi gambar dengan single channel
def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = np.linalg.svd(channelDataMatrix) #np.linalg.svd(channelDataMatrix) #jabarin SVD nya
    aChannelCompressed = np.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
    k = singularValuesLimit

    leftSide = np.matmul(uChannel[:, 0:k], np.diag(sChannel)[0:k, 0:k])
    aChannelCompressedInner = np.matmul(leftSide, vhChannel[0:k, :])
    aChannelCompressed = aChannelCompressedInner.astype('uint8')
    return aChannelCompressed


# MAIN PROGRAM:
print('*** Image Compression Using SVD Method ***\n')

# Input nama file
filename = input("Masukkan nama file: ")
matriksMerah, matriksHijau, matriksBiru, originalImage = openImage(filename)

# Image width and height
imageWidth, imageHeight = originalImage.size

# Input tingkat kompresi
ratio = int(input("Masukkan tingkat kompresi: "))

mr = imageHeight
mc = imageWidth
originalSize = mr * mc * 3

# Menghitung ukuran gambar setelah kompresi
compressedSize = int ((100-ratio)/100*originalSize)

# Menghitung jumlah nilai singular yang dapat digunakan
singularValuesLimit = int (compressedSize/(3*(1 + mr + mc)))

aRedCompressed = compressSingleChannel(matriksMerah, singularValuesLimit)
aGreenCompressed = compressSingleChannel(matriksHijau, singularValuesLimit)
aBlueCompressed = compressSingleChannel(matriksBiru, singularValuesLimit)

imr = Image.fromarray(aRedCompressed, mode=None)
img = Image.fromarray(aGreenCompressed, mode=None)
imb = Image.fromarray(aBlueCompressed, mode=None)

# Membuat matriks RGB
newImage = Image.merge("RGB", (imr, img, imb))

# Menampilkan gambar sebelum dan sesudah kompresi
originalImage.show()
newImage.show()

# Menampilkan perbandingan ukuran
print('Original size:', originalSize, 'pixels')
print('Compressed size:', compressedSize, 'pixels')
print('Compressed image size is ' + str(ratio) + '% of the original image.')

# Menyimpan gambar
save = input('Do you wanna save it? (Y/N) ')
if (save == 'Y'):
    newfilename = input('Masukkan nama file baru: ')
    newImage.save(fp=newfilename)

print('DONE - Compressed the image! Over and out!')