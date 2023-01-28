import cv2
import numpy as np


def colorDetection(frame, upColor, lowColor):
    into_hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # changing the color format from BGr to HSV 
    b_mask=cv2.inRange(into_hsv,lowColor,upColor)
    # creating the mask using inRange() function
    # this will produce an image where the color of the objects
    # falling in the range will turn white and rest will be black
    color=cv2.bitwise_and(frame,frame,mask=b_mask)
    into_hsv =cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    return color

def openCam(cam, upColor, lowColor):
    cap = cv2.VideoCapture(cam)
  
    while 1:
        ret,frame =cap.read() 
        cv2.imshow('Original',frame) # to display the original frame
        isFound = colorDetection(frame, upColor, lowColor)
        cv2.imshow('mask',isFound) # to display the original frame

        if cv2.waitKey(1)==27:
            break
        # this function will be triggered when the ESC key is pressed
        # and the while loop will terminate and so will the program
    cap.release()

    cv2.destroyAllWindows()