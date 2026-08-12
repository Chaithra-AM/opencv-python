import cv2
import numpy as np

# Create a blank image
img = np.zeros((500, 800, 3), dtype=np.uint8)

# Create colour stripes
img[:, 0:133] = (255, 0, 0)       # Blue
img[:, 133:266] = (0, 255, 0)     # Green
img[:, 266:399] = (0, 0, 255)     # Red
img[:, 399:532] = (0, 255, 255)   # Yellow
img[:, 532:665] = (255, 0, 255)   # Magenta
img[:, 665:800] = (255, 255, 0)   # Cyan

cv2.imshow("Color Stripes", img)

cv2.waitKey(0)
cv2.destroyAllWindows()