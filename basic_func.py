import cv2 as cv

image = cv.imread("Photos/park.jpg")
cv.imshow("Cat", image)

# convertir une image en couleur grise
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Brouiller une image/ Blur

blur = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade / cascade de bord
canny = cv.Canny(image, 125, 175) #  cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image / dilater
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding / erosion
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

# Resize
resized = cv.resize(image, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# CROPPING /recadrage
cropped = image[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)