import cv2 as cv
import numpy as np

img = cv.imread('UofT.jpg')

# translate
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
translated = translate(img, 100, 100)
cv.imshow('tr', translated)

# rotate
def rotate(img, angle, rotPoint = None):
    (heigh, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, heigh//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, heigh)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 180)
cv.imshow('rotated', rotated)

#Flipping
Flip = cv.flip(img, 0)
cv.imshow('Flip', Flip)

cv.waitKey(0)