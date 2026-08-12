import cv2
import numpy as np
import math

# Create white canvas
img = np.ones((600, 800, 3), dtype=np.uint8) * 255

drawing = False
start_x = 0
start_y = 0

shape = "rectangle"


def draw_shape(event, x, y, flags, param):
    global drawing, start_x, start_y, img

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x = x
        start_y = y

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        if shape == "rectangle":
            cv2.rectangle(
                img,
                (start_x, start_y),
                (x, y),
                (255, 0, 0),
                3
            )

        elif shape == "circle":
            radius = int(
                math.sqrt(
                    (x - start_x) ** 2 +
                    (y - start_y) ** 2
                )
            )

            cv2.circle(
                img,
                (start_x, start_y),
                radius,
                (0, 0, 255),
                3
            )


# Create window
cv2.namedWindow("Mouse Click Shapes")

# Connect mouse function
cv2.setMouseCallback("Mouse Click Shapes", draw_shape)


while True:

    # Show canvas
    cv2.imshow("Mouse Click Shapes", img)

    key = cv2.waitKey(1) & 0xFF

    # Press R for rectangle
    if key == ord("r"):
        shape = "rectangle"
        print("Rectangle selected")

    # Press C for circle
    elif key == ord("c"):
        shape = "circle"
        print("Circle selected")

    # Press Q to quit
    elif key == ord("q"):
        break


cv2.destroyAllWindows()