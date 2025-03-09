import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow("Park", img)

# Translation
def translate(img, x, y):
                        
    transMat = np.float32([[1,0,x], [0, 1, y]])
                    #  width    height
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 100)

"""
-x -> gauche
-y -> haut
x -> droit
y -> bas
"""

cv.imshow("Translated", translated)


# Rotation

def rotation(img, angle, pointRotation=None):
    (height, width) = img.shape[:2]

    if pointRotation is None:
        pointRotation = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(pointRotation, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotation(img, 50) # -50
cv.imshow("Rotation de l'image", rotated)

# Resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resized)

# Flipping an image
flip = cv.flip(img, -1) # 0
cv.imshow("Flip", flip)

# cropping
cropped = img[200:400, 300:400]
cv.imshow('Recadrage', cropped)

cv.waitKey(0)