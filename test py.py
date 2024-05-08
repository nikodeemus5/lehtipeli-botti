import cv2
import numpy as np
from matplotlib import pyplot as plt
import keyboard
import pyautogui # type: ignore


#gemi tunnistus
img_rgb = cv2.imread('screenshot.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

trade = ['gem.png','cheese.png']
for i in trade:
    template = cv2.imread(i,0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    f = set()

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

        sensitivity = 100
        f.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

    cv2.imwrite('res.png',img_rgb)

#laskuri
found_count = len(f)
print(found_count)

while True:
    if keyboard.is_pressed('f4'):
        print("trade bot käynnistetty.")
        pyautogui.moveTo(400, 870)