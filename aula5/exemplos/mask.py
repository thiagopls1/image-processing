import cv2
import numpy as np

img = cv2.imread("/home/thiago_lins/Pictures/Neofetch/gato.jpg", -1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.imshow("Imagem Original", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([80, 0, 0])
upper_blue = np.array([140, 255, 129])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Máscara", mask)
cv2.imshow("Resultado", result)
cv2.waitKey(0)
