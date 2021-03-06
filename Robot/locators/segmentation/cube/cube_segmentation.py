import cv2
import numpy


class CubeSegmentor():

    def __init__(self):
        self._lower_hsv_values = [0, 0, 0]
        self._upper_hsv_values = [0, 0, 0]

    def set_lower_hsv_values(self, value):
        self._lower_hsv_values = value

    def set_upper_hsv_values(self, value):
        self._upper_hsv_values = value

    def segment_cube(self, img):
        # Convert BGR image to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of yellow color in HSV
        lower = numpy.array(self._lower_hsv_values)
        upper = numpy.array(self._upper_hsv_values)

        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(img_hsv, lower, upper)

        # Apply erosion + opening
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
        mask = cv2.dilate(cv2.erode(mask, kernel), kernel)

        # Bitwise-AND mask and original image
        extracted_cube = cv2.bitwise_and(img, img, mask=mask)

        return extracted_cube
