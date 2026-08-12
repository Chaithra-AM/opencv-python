import cv2

cap = cv2.VideoCapture(0)

drawing = False
start_point = None
lines = []


def mouse_event(event, x, y, flags, param):
    global drawing, start_point, lines

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        end_point = (x, y)

        # Store the line
        lines.append((start_point, end_point))


cv2.namedWindow("Live Video Drawing")
cv2.setMouseCallback("Live Video Drawing", mouse_event)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Draw all previously created lines
    for start, end in lines:
        cv2.line(
            frame,
            start,
            end,
            (255, 0, 255),   # Magenta
            3
        )

    cv2.imshow("Live Video Drawing", frame)

    key = cv2.waitKey(1) & 0xFF

    # Clear all lines
    if key == ord('c'):
        lines.clear()

    # Quit
    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()