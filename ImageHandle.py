import cv2
print(cv2.__version__)

img = cv2.imread('Images/pinkPanther.jpg', 0)
print(img)
print(img.shape)

x, y = img.shape

for i in range(x):
    for j in range(y):
        if(i == 0):
            img[i:i+10, j:j+10] = [0]
        elif(i == (x-10)):
            img[i:i+10, j:j+10] = [0]
        elif(j == 0):
            img[i:i+10, j:j+10] = [0]
        elif(j == (y-10)):
            img[i:i+10, j:j+10] = [0]


cv2.imshow("Slogo", img)
cv2.waitKey(0)