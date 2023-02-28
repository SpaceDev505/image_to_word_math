import torch
import easyocr
import os

import cv2

# perform character recognition
# specify languages and other configs
reader = easyocr.Reader(['en'])
import cv2
import os

image = cv2.imread('3.jpg')
results = reader.readtext(image)

# draw rectangle on easyocr results
for res in results:
    top_left = (int(res[0][0][0]), int(res[0][0][1])) # convert float to int
    bottom_right = (int(res[0][2][0]), int(res[0][2][1])) # convert float to int
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
    cv2.putText(image, res[1], (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

# write image
# cv2.imshow('imge', image)
cv2.imwrite(f'out.jpg', image)