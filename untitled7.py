# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1So5kG92K2qC7EEKU8HWtchZVPlee_Kk9
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
from google.colab import files
import cv2
print("Iltimos, faylni tanlang:")
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
image = cv2.imread(file_name)
if image is None:
    print("Rasm fayli topilmadi. Iltimos, boshqa fayl tanlang.")
else:
    print("Rasm muvaffaqiyatli yuklandi!")
    cv2_imshow(image)
    resized_image = cv2.resize(image, (300, 300))
    print("O‘lchami o‘zgartirilgan rasm:")
    cv2_imshow(resized_image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Kulrang formatdagi rasm:")
    cv2_imshow(gray_image)
    blur_image = cv2.blur(image, (5, 5))
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
    print("Oddiy blur rasm:")
    cv2_imshow(blur_image)
    print("Gaussian blur rasm:")
    cv2_imshow(gaussian_blur)
    edges = cv2.Canny(gray_image, 100, 200)
    print("Chetlar aniqlangan rasm:")
    cv2_imshow(edges)
    cv2.line(image, (0, 0), (300, 300), (255, 0, 0), 5)
    cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)
    cv2.putText(image, 'Hello, OpenCV!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    print("Chiziqlar va matn qo‘shilgan rasm:")
    cv2_imshow(image)
    cv2.imwrite('gray_image.jpg', gray_image)
    cv2.imwrite('blur_image.jpg', blur_image)
    cv2.imwrite('edges_detected.jpg', edges)
    print("Rasmlar muvaffaqiyatli saqlandi!")