import cv2
import numpy as np

# Create a white image
image = np.ones((400, 600, 3), dtype=np.uint8) * 255

# Draw shapes on the image
cv2.rectangle(image, (100, 100), (300, 300), (255, 0, 0), -1)
cv2.circle(image, (450, 200), 80, (0, 0, 255), -1)

# Resize the image
resized = cv2.resize(image, (400, 300))

# Rotate the original image by 90 degrees
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)
cv2.imshow("Rotated Image", rotated)

# Save the manipulated images
cv2.imwrite("resized.jpg", resized)
cv2.imwrite("rotated.jpg", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()