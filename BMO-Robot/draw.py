import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Empty blank', blank)
# img = cv.imread('UofT.png')
# cv.imshow('UofT', img)


# 1. Pain the image acertain colour

blank[200:300, 300:400] = 0, 0, 225
cv.imshow('Green', blank)

# 2. Draw a rectangle

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness =-1)
cv.imshow("Rectangle", blank)

# 3. Draw a Circle

center = (blank.shape[1]//2, blank.shape[0]//2)
cv.circle(blank, center, 40, (255, 0, 0), thickness = -1)
cv.imshow('Circle', blank)

# 4. Draw a line

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness = 2)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Akhmet!!!', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)



# Color Palette in BGR format
# RED = (0, 0, 255)
# GREEN = (0, 255, 0) 
# BLUE = (255, 0, 0)
# YELLOW = (0, 255, 255)
# CYAN = (255, 255, 0)
# MAGENTA = (255, 0, 255)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (128, 128, 128)
# ORANGE = (0, 165, 255)
# PINK = (203, 192, 255)
# PURPLE = (128, 0, 128)
# BROWN = (19, 69, 139)
# GOLD = (0, 215, 255)
# MAROON = (0, 0, 128)
# NAVY = (128, 0, 0)
# OLIVE = (0, 128, 128)
# SILVER = (192, 192, 192)
# TEAL = (128, 128, 0)
# VIOLET = (226, 43, 138)
# SKYBLUE = (235, 206, 135)
# INDIGO = (130, 0, 75)
# LIME = (0, 255, 0)