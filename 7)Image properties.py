import cv2
import numpy as np

# Create an image
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Add a rectangle
cv2.rectangle(image, (100, 100), (500, 300), (0, 255, 0), -1)

# Get image properties
height, width, channels = image.shape
size = image.size
data_type = image.dtype

# Display properties
print("Image Width:", width)
print("Image Height:", height)
print("Number of Channels:", channels)
print("Image Size:", size)
print("Data Type:", data_type)

# Display image
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()