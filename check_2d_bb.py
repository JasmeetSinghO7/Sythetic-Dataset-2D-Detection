# BY ai_99 (02-08-2022)
# Check 2D Bounding Box.

import glob
import numpy as np
import cv2
import os

image_path = r"./rgb"  # path to images directory

images = glob.glob(os.path.join(image_path, "*.png"))
txt = glob.glob(os.path.join(image_path, "*.txt"))

for i in range(0, len(images)):
    
    img = cv2.imread(images[i])
    anno = np.loadtxt(txt[i], dtype=int)
    
    for j in anno:
        pt1 = (j[1], j[2])
        pt2 = (j[3] - j[1], j[4] - j[2])
        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

    cv2.imshow('Bounding Box Detection Window', img)
    if cv2.waitKey() == ord('q'):
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()
