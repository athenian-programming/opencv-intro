import cv2
import imutils
import numpy as np


def main():
    ball_height = 60
    ball_width = 60

    frame = cv2.imread('./images/messi.jpg')
    height, width = frame.shape[:2]

    ball = frame[282:(282 + ball_height), 333:(333 + ball_width)]

    # Create a blank canvas
    canvas1 = np.zeros((height, width, 3), dtype="uint8")
    # Paste the ball
    canvas1[170:(170 + ball_height), 150:(150 + ball_width)] = ball

    # Create a blank canvas
    canvas2 = np.zeros((ball_height, ball_width, 3), dtype="uint8")
    # Paste the ball
    canvas2[0:ball_height, 0:ball_width] = ball

    # Resize to new canvas
    canvas3 = imutils.resize(canvas2, width=400)

    # Paste 2nd ball
    frame[270:(270 + ball_height), 100:(100 + ball_width)] = ball

    # Paste 3rd ball
    # frame[270:(270 + ball_height), 20:(20 + ball_width)] = ball

    # Display images
    cv2.imshow('canvas1', canvas1)
    cv2.imshow('canvas2', canvas2)
    cv2.imshow('canvas3', canvas3)
    cv2.imshow('Frame', frame)

    # Wait for a keystroke
    cv2.waitKey(0)

    # Clean up
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
