import cv2

# OpenCV formato: B G R ao invés de R G B

# Abre e mostra a imagem
img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", 1)
print(img[0][0])
cv2.imshow(winname="Janela", mat=img)
cv2.waitKey(0)

cv2.imwrite('./output/imagem1.jpg', img)

# resize sem proporção
img_resized = cv2.resize(img, (400, 225))
cv2.imwrite('./output/imagem2_resize.jpg', img_resized)

# resize com proporção
img_resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imwrite('./output/imagem3_resize.jpg', img_resized)
# rotaçao
img_rotate = cv2.rotate(img_resized, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('./output/imagem4_rotate.jpg', img_rotate)
# cv2.imshow(img)

height, width, channel = img.shape

for i in range(height):
    for j in range(width):
        img[i][j] = ([int(img[i][j][0]*0.5), img[i][j][1], img[i][j][2]])

cv2.imwrite('./output/imagem5_menos_azul.jpg', img)
