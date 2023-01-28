import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H", "frame", 0, 255, nothing)
cv2.createTrackbar("S", "frame", 255, 255, nothing)
cv2.createTrackbar("V", "frame", 255, 255, nothing)

img_hsv = np.zeros((250,500,3), np.uint8)

while True:
    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    img_hsv[:] = (h,s,v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("deneme", img_bgr)
    if cv2.waitKey(1)==27:
            break
        # this function will be triggered when the ESC key is pressed
        # and the while loop will terminate and so will the program


cv2.destroyAllWindows()