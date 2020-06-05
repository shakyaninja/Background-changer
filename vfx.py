import cv2
import argparse
import numpy as np

cap = cv2.VideoCapture(0)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="PATH to image")
args = vars(ap.parse_args())
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of green color in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)
    inverted_mask = cv2.bitwise_not(mask)
    picture = cv2.imread(args["image"])
    print(picture)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_or(frame, frame, mask=mask)
    # masked correctly but in black
    res1 = cv2.bitwise_and(frame, frame, mask=inverted_mask)
    # res3 = cv2.bitwise_xor(res1, mask)
    # res2 = cv2.bitwise_or(res1, picture, mask=mask)
    res2 = cv2.bitwise_or(picture, picture, mask=mask)
    res3 = cv2.bitwise_xor(res1, res2)
    # cv2.imshow('frame', frame)
    cv2.imshow('picture', picture)
    # mask_pic = cv2.bitwise_and(mask, picture)
    # cv2.imshow('mask', mask)
    # cv2.imshow('mask_pic', mask_pic)
    # cv2.imshow('res', res)   # greenscreen only
    # cv2.imshow('res1', res1)  # person only
    # cv2.imshow('res2', res2)  # person only
    cv2.imshow('res3', res3)  # person only
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
