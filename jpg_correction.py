import cv2
import numpy as np
import base64

colors = {(255,255,255):"white",
          (0,0,255):"red",
          (0,255,0):"green",
          (255,0,0):"blue",
          (0,255,255):"yellow",
          (255,0,255):"purple",
          (255,255,0):"aqua",
          (0,0,0):"black"}

def read_image(input_text):
    img = cv2.imdecode(np.frombuffer(base64.b64decode(input_text), dtype=np.uint8), cv2.IMREAD_COLOR)
    return img


image = read_image(input())
image = np.where(image > 200, 255, 0)
x, y = map(int, input().split())

print(colors[tuple(image[y, x])])
