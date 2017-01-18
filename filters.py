import datetime

import cv2
import imutils

import camera
import opencv_utils as utils

if __name__ == "__main__":
    cam = camera.Camera()
    try:
        cnt = 0
        while cam.is_open():

            frame = cam.read()
            frame = imutils.resize(frame, width=600)

            flipped = cv2.flip(frame, 0)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            text = 'Frame #: {0}'.format(cnt)
            cv2.putText(frame, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, (.55 if utils.is_raspi() else .75), utils.RED,
                        2)

            # Display images
            cv2.imshow('Flipped', flipped)
            cv2.imshow('Gray', gray)
            cv2.imshow('HSV', hsv)
            cv2.imshow('Original', frame)

            key = cv2.waitKey(30) & 0xFF

            if key == ord('q'):
                break
            elif key == ord('s') or key == ord(' '):
                file_name = "img-{0}.png".format(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
                cv2.imwrite(file_name, frame)
                print("Wrote image to {0}".format(file_name))

            cnt += 1
    finally:
        cv2.destroyAllWindows()
        if cam.is_open():
            cam.close()
