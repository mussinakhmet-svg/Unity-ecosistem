import cv2 as cv
import numpy as np

img = cv.imread('UofT.jpg')

# 1. converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(img, 125, 127)
# cv.imshow("edges", canny)

# 4. Dilating the img
dilated = cv.dilate(canny, (3, 3), iterations = 1)
cv.imshow('Dilated', dilated)

# 5. Eroding
eroded = cv.erode(dilated, (3, 3), iterations = 3)
cv.imshow('eroded', eroded)

# 6. resize
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow ('Resized', resized)

# 7. Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)




# Video
# def rescaleframe(frame, scale = 0.30):
#     width = int (frame.shape[1] * scale)
#     height = int (frame.shape[0] * scale)

#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# capture = cv.VideoCapture('shortvideoofadog.mp4')
# while True:

#     isTrue, frame = capture.read()
#     frame_resized = rescaleframe(frame)

#     cv.imshow('Videodog', frame)
#     cv.imshow('Resized video', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break;
# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)