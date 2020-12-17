path = "C:\\Users\\18mia\\Desktop\\CS330\\images\\AAA.jpg"
# import the necessary packages
#https://www.youtube.com/watch?v=C-WP0IqXVP0&t=27s&ab_channel=GaganPanwar
#https://www.youtube.com/watch?v=SrZuwM705yE&ab_channel=Murtaza%27sWorkshop-RoboticsandAI
#http://dsynflo.blogspot.com/2014/10/opencv-qr-code-detection-and-extraction.html
#https://www.pyimagesearch.com/2014/11/24/detecting-barcodes-images-python-opencv/ TUTORIAL
#https://stackoverflow.com/questions/51167768/sobel-edge-detection-using-opencv SOBEL OPERATOR CODE

from pyzbar import pyzbar
import numpy as np
import cv2 as cv
import imutils
import argparse
import matplotlib.pyplot as plt
#c# very old 
cap = cv.VideoCapture(0)
if not cap.isOpened(): 
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #compute the scharr gradient magnituede representation of the images
    # Display the resulting frame
    
    #Sobel derivitive filter
    ddepth = cv.CV_32F if imutils.is_cv2() else cv.CV_32F
    gradX = cv.Sobel(gray, ddepth=ddepth, dx=1, dy = 0, ksize = -1)
    gradY = cv.Sobel(gray, ddepth=ddepth, dx = 0, dy = 1, ksize = -1)
    abs_grad_x = cv.convertScaleAbs(gradX)
    abs_grad_y = cv.convertScaleAbs(gradY)
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    #gradient_magnitude = np.sqrt(np.square(gradX) + np.square(gradY))
    
    #gradient_magnitude *= 255.0 / gradient_magnitude.max()
    #---------------------------sobel Matrix transformation complete
    #start Blurring
    blurred = cv.blur(grad, (9, 9))
    (_, thresh) = cv.threshold(blurred, 130, 130, cv.THRESH_BINARY)
    
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (21, 7))
    closed = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
    
    closed = cv.erode(closed, None, iterations = 4)
    closed = cv.dilate(closed, None, iterations = 4)
    #find contours in the threshnold image
    cnts = cv.findContours(closed.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow('frame', grad)
    if cv.waitKey(1) == ord('q'):
        break