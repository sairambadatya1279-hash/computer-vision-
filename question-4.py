import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Remove mirror effect
    frame = cv2.flip(frame, 1)

    h, w = frame.shape[:2]

    # Half-size grayscale display
    half = cv2.resize(frame, (w // 2, h // 2))
    gray = cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Half Size Grayscale", gray)

    # Quarter-size image for 2x2 grid
    small = cv2.resize(frame, (w // 2, h // 2))

    # Top-Left: Original
    tl = small.copy()

    # Top-Right: Vertically Flipped
    tr = cv2.flip(small, 0)

    # Bottom-Left: HSV
    bl = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)

    # Bottom-Right: Red Channel Only
    br = np.zeros_like(small)
    br[:, :, 2] = small[:, :, 2]

    # Create 2x2 grid
    top = cv2.hconcat([tl, tr])
    bottom = cv2.hconcat([bl, br])
    final = cv2.vconcat([top, bottom])

    cv2.imshow("4 Window Display", final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()