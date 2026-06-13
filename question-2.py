import cv2
import time

cap = cv2.VideoCapture(0)

prev_time = time.time()
count = 0

while True:
    ret, frame = cap.read()

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam Feed", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite(f"image_{count}.png", frame)
        print("Image Saved")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()