import cv2

cap = cv2.VideoCapture(0)

largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')

print(largura)
print(altura)

# nome arquivo, codec, FR, tamanho
gravador = cv2.VideoWriter('meu_video1.avi', codec, 20, (largura, altura))

while True:
  ret, frame = cap.read()
  frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gravador.write(frame)

  if not ret:
    print('erro na captura')
    break
  
  cv2.imshow('webcam', frame)
  #cv2.imshow('webcam', frame_grey)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
gravador.release()
cv2.destroyAllWindows