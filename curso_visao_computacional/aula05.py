import cv2

tamanho = 9
imgs = ['ruido.png', 'eu_ruido.png']
img = cv2.imread(imgs[1])

blur_media = cv2.blur(img, (tamanho, tamanho))
blur_galciano = cv2.GaussianBlur(img, (tamanho, tamanho), 0)
blur_mediana = cv2.medianBlur(img, tamanho)

cv2.imshow('Original', img)
cv2.imshow('Média', blur_media)
cv2.imshow('Gauciana', blur_galciano)
cv2.imshow('Mediana', blur_mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()