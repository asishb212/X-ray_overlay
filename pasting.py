import numpy as np
import cv2
import matplotlib.pyplot as plt

one = cv2.imread("base/1.jpg")
two = cv2.imread("base/2.jpg")
three = cv2.imread("base/3.jpg")
four = cv2.imread("base/4.jpg")
zero = cv2.imread("base/0.jpg")

imgs = [zero, one, two, three, four]

oneb = cv2.imread("background_images/BAGGAGE_20180811_175323_83216_B_1.jpg")
twob = cv2.imread("background_images/BAGGAGE_20180811_175328_83216_A_1.jpg")
threeb = cv2.imread("background_images/S0210209058_20180811232942_L-1_1.jpg")
fourb = cv2.imread("background_images/S0300542812_20180822020845_L-10_1.jpg")
fiveb = cv2.imread("background_images/S0320365070_20180821160850_L-12_5.jpg")

bkgs = [oneb, twob, threeb, fourb, fiveb]


def isolate(image):
    img = np.copy(image)
    lower = np.array([240, 240, 240])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    img[mask != 0] = [0, 0, 0]
    return (img, mask)


imgs[0] = cv2.copyMakeBorder(zero, 87, 0, 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
imgs[1] = imgs[1][50:bkgs[1].shape[0]+50, :, :]
imgs[2] = imgs[2][50:bkgs[2].shape[0]+50, :, :]
imgs[3] = imgs[3][:bkgs[3].shape[0], :, :]
imgs[4] = imgs[4][118:bkgs[4].shape[0]+118, :, :]

for i in range(5):
    isolate_image, mask = isolate(imgs[i])
    bkgs[i][mask == 0] = [0, 0, 0]
    isolate_image = np.multiply(isolate_image, 0.8)
    final = bkgs[i]+isolate_image
    cv2.imwrite(str(i)+".png", final)
