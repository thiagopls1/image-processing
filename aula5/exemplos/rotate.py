import cv2

# OpenCV formato: B G R ao invés de R G B

# Abre e mostra a imagem
img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", 1)
print(img[0][0])

img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow(winname="Janela", mat=img)
cv2.waitKey(0)
