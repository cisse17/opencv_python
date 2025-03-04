import cv2 as cv

"""Lire une Photo"""
# img  = cv.imread('Photos/cat.jpg')

# cv.imshow('Chat', img)


"""Lire une Vidéo"""

capture = cv.VideoCapture('Videos/growth_event.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # press lettre d pour stopper la vidéo
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)