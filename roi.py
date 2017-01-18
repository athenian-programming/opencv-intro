import cv2
import imutils
import numpy as np

if __name__ == "__main__":
    ball_height = 60
    ball_width = 60

    frame = cv2.imread('./images/messi.jpg')
    height, width = frame.shape[:2]

    ball = frame[282:(282 + ball_height), 333:(333 + ball_width)]

    frame[270:(270 + ball_height), 100:(100 + ball_width)] = ball

    canvas1 = np.zeros((height, width, 3), dtype="uint8")
    canvas1[170:(170 + ball_height), 150:(150 + ball_width)] = ball

    canvas2 = np.zeros((ball_height, ball_width, 3), dtype="uint8")
    canvas2[0:ball_height, 0:ball_width] = ball

    canvas3 = imutils.resize(canvas2, width=400)

    # Display images
    cv2.imshow('Frame', frame)
    cv2.imshow('canvas1', canvas1)
    cv2.imshow('canvas2', canvas2)
    cv2.imshow('canvas3', canvas3)

    # Wait for a keystroke
    cv2.waitKey(0)

    cv2.destroyAllWindows()
