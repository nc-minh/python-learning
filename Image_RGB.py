import cv2
from datetime import datetime


img = cv2.imread('Images/pinkPanther.jpg')

x, y, _= img.shape
print(x, y)
now = datetime.now()
print('start: ', now.strftime("%H:%M:%S"))

for i in range(x):
    for j in range(y):
        # print(img[i, j])
        b, g, r = img[i, j]
        if(r > 220 and r < 255):
            img[i, j] = [255, 0, 0]

now = datetime.now()
print('end: ', now.strftime("%H:%M:%S"))

cv2.imshow("Slogo", img)
cv2.waitKey(0)
