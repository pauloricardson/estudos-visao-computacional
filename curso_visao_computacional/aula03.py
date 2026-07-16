import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    vermelho_escuro = np.array([160, 50, 50])
    vermelho_claro = np.array([179, 255, 255])

    mascara = cv2.inRange(hsv, vermelho_escuro, vermelho_claro)

    resultado = cv2.bitwise_and(frame, frame, mask=mascara)

    #cv2.imshow('camera original', frame)
    cv2.imshow('camera original', resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows