import cv2

# OpenCV formato: B G R ao invés de R G B

# Abre e mostra a imagem
img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", 1)
print(img[0][0])

img_crop = img[0:150, 0:180]

cv2.imshow(winname="Janela", mat=img_crop)
cv2.waitKey(0)
