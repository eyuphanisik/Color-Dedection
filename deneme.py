import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame =cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of red color in HSV
    lower_red = np.array([170, 100, 60])
    upper_red = np.array([183, 255, 255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask.astype(np.uint8)

    # Find contours in the binary image
    M = cv2.moments(mask)

    # Calculate the center of the object
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        # Object is not present in the frame
        cx, cy = 0, 0

    # Draw a circle at the center of the object
    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # Show the image"""
    cv2.imshow("Image", frame)
    if cv2.waitKey(1)==27:
            break
    
cv2.destroyAllWindows()