import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
from scipy import ndimage

one = cv2.imread("threat_images/BAGGAGE_20170522_113049_80428_A.jpg")
two = cv2.imread("threat_images/BAGGAGE_20170522_115645_80428_B.jpg")
three = cv2.imread("threat_images/BAGGAGE_20170523_085803_80428_D.jpg")
four = cv2.imread("threat_images/BAGGAGE_20170523_094231_80428_B.jpg")
five = cv2.imread("threat_images/BAGGAGE_20170524_075554_80428_B.jpg")

imgs = [one, two, three, four, five]

oneb = cv2.imread("background_images/BAGGAGE_20180811_175323_83216_B_1.jpg")
twob = cv2.imread("background_images/BAGGAGE_20180811_175328_83216_A_1.jpg")
threeb = cv2.imread("background_images/S0210209058_20180811232942_L-1_1.jpg")
fourb = cv2.imread("background_images/S0300542812_20180822020845_L-10_1.jpg")
fiveb = cv2.imread("background_images/S0320365070_20180821160850_L-12_5.jpg")

bkgs = [oneb, twob, threeb, fourb, fiveb]


def resize(image, cst):
    img = np.copy(image)
    aspect_ratio = cst/img.shape[1]
    dim = (cst, int(image.shape[0] * aspect_ratio))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized


def rotate(image):
    img = np.copy(image)
    img = ndimage.rotate(img, 45, cval=255)
    return img


csts = [i.shape[1] for i in bkgs]
opts = []
for i in range(5):
    opt = resize(rotate(imgs[i]), csts[i])
    cv2.imwrite("base/"+str(i)+".jpg", opt)
