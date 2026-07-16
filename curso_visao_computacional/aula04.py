import cv2

img1 = cv2.imread('paisagem_trem.jpg')
img2 = cv2.imread('logo.jpg')
#img1[100:150, 150:200] = [0, 0, 255]
#pixel = img1[100, 150]
#roi = img1[100:300, 150:350]
#soma = cv2.add(img1, img2)
#cv2.imshow('Soma direta', soma)

mersclagem = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
cv2.imshow('Soma direta', mersclagem)

#cv2.imshow('Roi', roi)

#print(f"Valor BGR do Pixel: {pixel}")

cv2.waitKey(0)
cv2.destroyAllWindows()