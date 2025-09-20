import cv2

# OpenCV formato: B G R ao invés de R G B

# Abre e mostra a imagem
img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", 1)
print(img[0][0])

img_crop = img[0:150, 0:180]
img[150:300, 180:360] = img_crop

cv2.imshow(winname="Janela", mat=img)
cv2.waitKey(0)
