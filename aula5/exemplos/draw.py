import cv2

img = cv2.imread('/home/thiago_lins/Pictures/Neofetch/gato.jpg', -1)
height, width, channels = img.shape

img = cv2.line(img, (0, 0), (width, height), (255, 0, 0), 10)
img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'BCC :)', (10, height - 10), font, 2, (0, 0, 255), 5, cv2.LINE_AA)

cv2.imshow(winname="Janela", mat=img)
cv2.waitKey(0)
