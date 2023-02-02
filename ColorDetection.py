import cv2
import numpy as np
import socket
import time

def colorDetection(frame, upColor, lowColor):

    into_hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # changing the color format from BGr to HSV 
    b_mask=cv2.inRange(into_hsv,lowColor,upColor)
    # creating the mask using inRange() function
    # this will produce an image where the color of the objects
    # falling in the range will turn white and rest will be black   
    return b_mask

def isFind(color):
        
        if len(color[color > 20]) > 10000:
            return True
        return False
        
def openCam(cam, upColor, lowColor):
    cap = cv2.VideoCapture(cam)
    # UDP soketi oluşturma
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Gönderilecek adresi tanımlama
    address = ('localhost', 1453)
    while 1:
        ret,frame =cap.read() 
        #cv2.imshow('Original',frame) # to display the original frame
        color = colorDetection(frame, upColor, lowColor)
        isFound = isFind(cv2.bitwise_and(frame,frame,mask=color))

        color = color.astype(np.uint8)
        M = cv2.moments(color)

        # Calculate the center of the object
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            # Object is not present in the frame
            cx, cy = 0, 0
        print(cx, cy)
        # Draw a circle at the center of the object
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
        
        send_data = bytes(str(isFound), encoding='utf-8')
        sock.sendto(send_data, address)
        print(send_data)
        # Her göndermeden sonra bekleme
        cv2.imshow("no", frame)
        if cv2.waitKey(1)==27:
            break
        # this function will be triggered when the ESC key is pressed
        # and the while loop will terminate and so will the program
    cap.release()

    cv2.destroyAllWindows()

    