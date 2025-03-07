import cv2 as cv
img  = cv.imread('Photos/cat.jpg')

cv.imshow('Chat', img)



def rescaleFrame(frame, scale=0.75):
    # cette methode fonctionne pr image, vidéo et live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



resized_img = rescaleFrame(img)
cv.imshow('Image reduit', resized_img)

capture = cv.VideoCapture('Videos/growth_event.mp4')


def changeRes(width, height):
    # cette methode fonctionne uniquement en live video
    capture.set(3, width)
    capture.set(5, height)


while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    # frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): # press lettre d pour stopper la vidéo
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)