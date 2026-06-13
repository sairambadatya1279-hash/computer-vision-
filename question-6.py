import cv2

# Start webcam
cap = cv2.VideoCapture(0)

blur = 1  # Initial blur level (must be odd)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (blur, blur), 0)

    # Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)

    # Display
    cv2.imshow("Edges", edges)

    key = cv2.waitKey(1) & 0xFF

    # Increase blur (softer edges)
    if key == ord('w'):
        blur += 2
        print("Blur Kernel Size:", blur)

    # Decrease blur (sharper edges)
    elif key == ord('s'):
        if blur > 1:
            blur -= 2
        print("Blur Kernel Size:", blur)

    # Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()