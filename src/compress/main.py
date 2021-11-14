import numpy as np
from PIL import Image
from lib import compressSingleChannel, imageRGB

# MAIN PROGRAM:
print('*** Image Compression Using SVD Method ***\n')

# Input nama file
filename = input("Masukkan nama file: ")
originalImage = Image.open(filename)
matriksMerah, matriksHijau, matriksBiru = imageRGB(filename)

# Image width and height
imageWidth, imageHeight = originalImage.size

# Input tingkat kompresi
ratio = int(input("Masukkan tingkat kompresi: "))

mr = imageHeight
mc = imageWidth
originalSize = mr * mc

# Menghitung ukuran gambar setelah kompresi
compressedSize = int (ratio/100*originalSize)

# Menghitung jumlah nilai singular yang dapat digunakan
singularValuesLimit = int (compressedSize/(1 + mr + mc))

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
