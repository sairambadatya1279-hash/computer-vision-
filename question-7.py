import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

led_on = False
pinch_detected = False

THRESHOLD = 40  # pinch distance

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, hand, mp_hands.HAND_CONNECTIONS
            )

            h, w, _ = frame.shape

            thumb = hand.landmark[4]
            index = hand.landmark[8]

            tx, ty = int(thumb.x * w), int(thumb.y * h)
            ix, iy = int(index.x * w), int(index.y * h)

            cv2.circle(frame, (tx, ty), 8, (255, 0, 0), -1)
            cv2.circle(frame, (ix, iy), 8, (0, 255, 0), -1)

            distance = math.hypot(ix - tx, iy - ty)

            # Toggle LED on pinch
            if distance < THRESHOLD and not pinch_detected:
                led_on = not led_on
                pinch_detected = True

            # Reset when fingers separate
            if distance > THRESHOLD + 20:
                pinch_detected = False

    # LED Indicator
    color = (0, 255, 0) if led_on else (0, 0, 255)
    text = "ON" if led_on else "OFF"

    cv2.circle(frame, (80, 80), 30, color, -1)
    cv2.putText(frame, text, (50, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                color, 2)

    cv2.imshow("LED Toggle with Pinch", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()