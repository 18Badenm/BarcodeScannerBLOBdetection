# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:24:55 2020

@author: 18mia
"""
import cv2 as cv
import numpy as np

def main():
    cap = cv.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #github page you can use xml trained files
        sobel = sobel(gray)
        cv.imshow('frame', sobel)
        if cv.waitKey(1) == ord('q'):
            break

def sobel(gray):
	Gx = [[-1 0 1, -2 0 2; -1 0 1]
	Gy = [-1 -2 -1; 0 0 0; 1 2 1]
	
	rows = size(A, 1)
	columns = size(A, 2)
    
	transform1 = np.dot(gray, Gx)
    transform2 = np.dot(gray, Gy)
    
    transform3 = sqrt(transform1^2+transform^2)
    
	return output_image
'''