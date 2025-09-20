import cv2

# OpenCV formato: B G R ao invés de R G B

# Abre e mostra a imagem
img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", -1)
width, height, channel = img.shape
img_resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# y, x
quadrantes = [
    [(0, height//2), (0, width//2)],            # Cima esquerda
    [(0, height//2), (width//2, (width))],      # Cima direita
    [(height//2, height), (0,width//2)],        # Baixo esq.
    [(height//2, height), (width//2, width)],   # Baixo dir.
]

for q in quadrantes:
    img[q[0][0]:q[0][1], q[1][0]:q[1][1]] = img_resized

# CE azul
for i in range(quadrantes[0][0][0], quadrantes[0][0][1]):
    for j in range(quadrantes[0][1][0], quadrantes[0][1][1]):
        img[i][j] = ([img[i][j][0], int(img[i][j][1]*0.5), int(img[i][j][2]*0.5)])

# CD vermelho
for i in range(quadrantes[1][0][0], quadrantes[1][0][1]):
    for j in range(quadrantes[1][1][0], quadrantes[1][1][1]):
        img[i][j] = ([int(img[i][j][0]*0.5), int(img[i][j][1]*0.5), img[i][j][2]])


# BE verde
for i in range(quadrantes[2][0][0], quadrantes[2][0][1]):
    for j in range(quadrantes[2][1][0], quadrantes[2][1][1]):
        img[i][j] = ([img[i][j][0]*0.5, img[i][j][1], int(img[i][j][2]*0.5)])

cv2.imshow(winname="Janela", mat=img)
cv2.waitKey(0)
