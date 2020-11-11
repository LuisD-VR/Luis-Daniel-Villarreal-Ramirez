import cv2
import numpy as np

img = cv2.imread('Circulo de colores.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

fucsia_bajos = np.array([145,50,50])
fucsia_altos = np.array([165,255,255])

verde_bajos = np.array([45,50,50])
verde_altos = np.array([65,255,255])

naranja_bajos = np.array([10,50,50])
naranja_altos = np.array([20,255,255])

mask_fucsia = cv2.inRange(hsv, fucsia_bajos, fucsia_altos)

mask_verde = cv2.inRange(hsv, verde_bajos, verde_altos)

mask_naranja = cv2.inRange(hsv, naranja_bajos, naranja_altos)

mask_union = mask_fucsia + mask_verde + mask_naranja

cv2.imshow('Original', img)
cv2.imshow('Fucsia+Naranja+Verde', mask_union)
print('\nPulsa cualquier tecla para cerrar las ventanas\n')
cv2.waitKey(0)
cv2.destroyAllWindows()
