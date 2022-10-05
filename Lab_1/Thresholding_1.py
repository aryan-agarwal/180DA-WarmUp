import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.VideoCapture(0)
while(1):
    _, frame = img.read()
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

    '''ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)'''

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    cv.imshow('thresh1',thresh1)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

