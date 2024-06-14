import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image


img_NZ_bgr = cv2.imread("data/New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
window1 = cv2.namedWindow('test')
# cv2.imshow(window1, img_NZ_bgr)
# cv2.waitKey(5000)
# cv2.destroyWindow(window1)

alive = True

while alive:
    cv2.imshow(window1, img_NZ_bgr)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        alive = False
cv2.destroyWindow(window1)

cv2.destroyAllWindows()