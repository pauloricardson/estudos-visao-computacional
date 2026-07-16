import cv2

imagens = ['texto_a.png', 'texto_b.png', 'placa_a.png', 'placa_b.png']

img = cv2.imread(imagens[3], 0)

ret, thresh_binario = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#ret, thresh_binario_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

thresh_adaptativo = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    199,
    10
)

cv2.imshow('Original', img)
cv2.imshow('Limiar Binário', thresh_binario)
#cv2.imshow('Limiar Binário Invertido', thresh_binario_inv)
cv2.imshow('Limiar Adaptativo', thresh_adaptativo)

cv2.waitKey(0)
cv2.destroyAllWindows()