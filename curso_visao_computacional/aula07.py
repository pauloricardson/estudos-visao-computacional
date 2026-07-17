import cv2

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    dif = cv2.absdiff(frame1, frame2)
    cinza = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(cinza, (5, 5), 0)
    _, thesh = cv2.threshold(blur, 20, 255,  cv2.THRESH_BINARY)
    dilat = cv2.dilate(thesh, None, iterations = 3)

    contornos, _ = cv2.findContours(dilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        if cv2.contourArea(contorno) < 5000:
            continue
        (x, y, w, h) = cv2.boundingRect(contorno)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print('ALERTA, movimento detectado')

    cv2.imshow('Diferenca', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows