
import cv2

# OpenCV formato: B G R ao invés de R G B

# Abre e mostra a imagem
img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", 1)
print(img[0][0])

# resize com proporção
img_resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

cv2.imshow(winname="Janela", mat=img_resized)
cv2.waitKey(0)
