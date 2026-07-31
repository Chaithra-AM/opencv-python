import cv2
import numpy as np

# Create a white canvas
img = np.ones((100, 800), dtype=np.uint8) * 255

# Draw 8 different gray shades
for i in range(8):
    shade = i * 36  # 0, 36, 72, ..., 252
    cv2.rectangle(img, (i * 100, 0), ((i + 1) * 100, 100), shade, -1)
    cv2.putText(img, str(shade), (i * 100 + 20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                255 - shade if shade < 128 else 0, 1)

cv2.imshow("Gray Shades", img)

cv2.waitKey(0)
cv2.destroyAllWindows()