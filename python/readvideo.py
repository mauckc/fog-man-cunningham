import cv2
import numpy as np
import math


cap = cv2.VideoCapture("sample-fog.mp4")

if (cap.isOpened() == False):
    print("Error opening video stream or file")

    # Read until video is completed
while(cap.isOpened()):
    # capture frame by frame
    ret, frame = cv2.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    #Break the loop
    else:
        break

# When procesing frames is done or user entered 'q'
cap.release()

# close all the frames
cv2.destroyAllWindows()
