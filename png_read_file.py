import cv2
import numpy as np

image = cv2.imread('RGB-image.png')

if image is not None:
    print(f"Прочитано изображение размером {image.shape}")
else:
    print("Ошибка чтения изображения")

cv2.imshow('Image',image) #'Image' - заголовок окна, img - переменная, содержащая изображение

# Для того, чтобы оставить в изображении один канал, необходимо воспользоваться
# срезом для массива NumPy:

blue_channel = image[:, :, 0]  # Синий канал
green_channel = image[:, :, 1]  # Зеленый канал
red_channel = image[:, :, 2]  # Красный канал

# Отображение окон
cv2.imshow('Original image', image)
cv2.imshow('Red channel', red_channel)
cv2.imshow('Green channel', green_channel)
cv2.imshow('Blue channel', blue_channel)

"""
cv2.imwrite(filename, image)
filename: строка, представляющая путь и имя файла, в который будет сохранено изображение. Расширение файла (например, .jpg, .png, .bmp) определяет формат сохраненного изображения.
image: массив NumPy, представляющий изображение, которое необходимо сохранить.
"""

cv2.waitKey(0) #ожидает нажатия любой клавиши
cv2.destroyAllWindows() #закроет окно перед завершением скрипта
