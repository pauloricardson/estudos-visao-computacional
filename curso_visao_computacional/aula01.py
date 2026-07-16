import cv2

imagem = cv2.imread('teste.jpg')

cv2.imshow('primeira imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()