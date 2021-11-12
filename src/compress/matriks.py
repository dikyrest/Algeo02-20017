import numpy as np
import sympy as sp
from PIL import Image

# FUNCTION DEFINTIONS:
# Mencari nilai eigen dan vektor eigen
def find_eig(A):
    M = sp.Matrix(A)
    E,D = M.diagonalize()
    numE = np.array(E, dtype=np.float32)
    numD = np.array(D, dtype=np.float32)
    numD = numD[::-1, ::-1]
    eigvec = numE[:, ::-1]
    eigvec = eigvec.T
    nor = np.linalg.norm(eigvec, axis=1)
    for i in range(eigvec.shape[0]):
        eigvec[i] = eigvec[i] / nor[i]
    eigvec = eigvec.T
    eigval = np.diag(numD)
    return eigval, eigvec

# Algoritma SVD
def SVD(A):
    AAt = np.dot(A, A.T)
    lval, lvec = find_eig(AAt)
    
    AtA = np.dot(A.T, A)
    rval, rvec = find_eig(AtA)
    
    row = A.shape[0]
    col = A.shape[1]
    sigma = np.zeros((row, col))
    for i in range(min(row, col)):
        sigma[i][i] = rval[i]**(1/2)

    return [lvec, sigma, rvec.T]

# Membuka gambar dan mengembalikan matriks berdasarkan channel (Red, Green, dan Blue)
def openImage(imagePath):
    imageOrigin = Image.open(imagePath)
    imageMatriks = np.array(imageOrigin)
    return [imageMatriks[:, :, 0], imageMatriks[:, :, 1], imageMatriks[:, :, 2], imageOrigin]

# Kompresi gambar dengan single channel
def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = SVD(channelDataMatrix) #np.linalg.svd(channelDataMatrix) #jabarin SVD nya
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