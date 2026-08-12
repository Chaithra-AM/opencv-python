import cv2

# Video settings
width = 800
height = 500
fps = 30

# Create a video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('car_motion.avi', fourcc, fps, (width, height))

# Create car-motion video
for x in range(-150, width + 50, 5):

    frame = 255 * __import__('numpy').ones(
        (height, width, 3), dtype=__import__('numpy').uint8
    )

    # Road
    cv2.rectangle(frame, (0, 350), (width, height), (80, 80, 80), -1)

    # Road lines
    for line_x in range(0, width, 100):
        cv2.rectangle(
            frame,
            (line_x, 420),
            (line_x + 50, 430),
            (255, 255, 255),
            -1
        )

    # Car body
    cv2.rectangle(
        frame,
        (x, 300),
        (x + 140, 360),
        (0, 0, 255),
        -1
    )

    # Car roof
    cv2.rectangle(
        frame,
        (x + 30, 260),
        (x + 110, 300),
        (0, 0, 255),
        -1
    )

    # Windows
    cv2.rectangle(
        frame,
        (x + 40, 265),
        (x + 65, 295),
        (200, 200, 200),
        -1
    )

    cv2.rectangle(
        frame,
        (x + 75, 265),
        (x + 100, 295),
        (200, 200, 200),
        -1
    )

    # Wheels
    cv2.circle(frame, (x + 35, 365), 20, (0, 0, 0), -1)
    cv2.circle(frame, (x + 105, 365), 20, (0, 0, 0), -1)

    # Add frame number
    cv2.putText(
        frame,
        "Car Motion - Frame Demonstration",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 0),
        2
    )

    # Write frame to video
    out.write(frame)

out.release()

print("Car motion video created successfully!")

# Open the created video
cap = cv2.VideoCapture("car_motion.avi")

frame_number = 0

while True:

    # Read video frame by frame
    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    # Display frame number
    cv2.putText(
        frame,
        "Frame: " + str(frame_number),
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 0),
        2
    )

    cv2.imshow("Car Motion Video", frame)

    # Press Q to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()