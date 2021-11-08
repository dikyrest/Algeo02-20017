import numpy as np
from matplotlib.image import imread

A = imread("doraemon.jpg")      # membaca gambar dengan format RGB
row = (A.shape)[0]              # tinggi gambar
col = (A.shape)[1]              # lebar gambar
R = np.zeros((row,col))
G = np.zeros((row,col))
B = np.zeros((row,col))

# memisahkan matriks Red, Green, Blue
for i in range(row):
    for j in range(col):
        R[i][j] = A[i][j][0]
        G[i][j] = A[i][j][1]
        B[i][j] = A[i][j][2]