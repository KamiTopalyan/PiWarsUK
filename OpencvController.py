import cv2
import numpy as np
class OpencvController:
    def __init__(self, colors) -> None:
        self.colors = colors
        
    def seperateColors(self, img, color):
        """
        Source: https://stackoverflow.com/a/72594725
        Separate the unwanted color from the image and display the result

        Args:
            img (img): image to be processed
            color (tuple): threshold values for the color to be kept
        """
        
        # threshold on orange
        lower, upper = self.colors[color]
        thresh = cv2.inRange(img, lower, upper)

        # apply morphology and make 3 channels as mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.merge([mask,mask,mask])

        # create 3-channel grayscale version
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        # blend img with gray using mask
        result = np.where(mask==255, img, gray)

        return result