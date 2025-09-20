import cv2
from random import randint

# OpenCV formato: B G R ao invés de R G B

# Abre e mostra a imagem
img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", 1)
print(img[0][0])
height, width, channel = img.shape

for i in range(height):
    for j in range(width):
        img[i][j] = ([randint(0, 255), randint(0, 255), randint(0, 255)])

cv2.imshow(winname="Janela", mat=img)
cv2.waitKey(0)
