import numpy as np
from PIL import Image

# FUNCTION DEFINTIONS:
# Membuka gambar dan mengembalikan matriks berdasarkan channel (Red, Green, dan Blue)
def openImage(imagePath):
    imOrig = Image.open(imagePath)
    im = np.array(imOrig)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue, imOrig]

# Kompresi gambar dengan single channel
def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = np.linalg.svd(channelDataMatrix) #jabarin SVD nya
    aChannelCompressed = np.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
    k = singularValuesLimit

    leftSide = np.matmul(uChannel[:, 0:k], np.diag(sChannel)[0:k, 0:k])
    aChannelCompressedInner = np.matmul(leftSide, vhChannel[0:k, :])
    aChannelCompressed = aChannelCompressedInner.astype('uint8')
    return aChannelCompressed

# Mencari nilai eigen
def find_eig_qr(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(100):
            Q,R = np.linalg.qr(X)
            pQ = np.dot(pQ,Q)
            X = np.dot(R,Q)
    return np.diag(X), pQ

# MAIN PROGRAM:
print('*** Image Compression using SVD - a demo\n')

# Input nama file
filename = input("Masukkan nama file: ")
aRed, aGreen, aBlue, originalImage = openImage(filename)

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

aRedCompressed = compressSingleChannel(aRed, singularValuesLimit)
aGreenCompressed = compressSingleChannel(aGreen, singularValuesLimit)
aBlueCompressed = compressSingleChannel(aBlue, singularValuesLimit)

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