import cv2
import numpy as np
from matplotlib import pyplot as plt
import keyboard
import pyautogui

gem_count = 0
cheese_count = 0
resourse_value = {}

#reunojen piirto
def piirto(img_rgb, loc, w, h, img_type):
    for pt in zip(*loc[::-1]):
        if img_type == 'gem':
            color = (0, 255, 0)  # Vihreä gemille
        elif img_type == 'cheese':
            color = (0, 0, 255)  # Punainen juustolle
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), color, 2)
        sensitivity = 100
        resourse_value.setdefault(img_type, set()).add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

#kuvan tunnistus
img_rgb = cv2.imread('screenshot.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

trade = ['gem.png','cheese.png']
for i in trade:
    template = cv2.imread(i, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    piirto(img_rgb, loc, w, h, i.split('.')[0])  # Talletetaan kuvatyyppi

    cv2.imwrite('res.png', img_rgb)

#laskuri
gem_count = len(resourse_value.get('gem', []))
cheese_count = len(resourse_value.get('cheese', []))

print('Gemei: ', gem_count)
print('Juustoja: ', cheese_count)

while True:
    if keyboard.is_pressed('f4'):
        print("trade bot käynnistetty.")
        pyautogui.moveTo(400, 870)