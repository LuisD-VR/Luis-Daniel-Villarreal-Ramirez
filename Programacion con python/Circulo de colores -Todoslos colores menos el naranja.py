import cv2
import numpy as np

img = cv2.imread('Circulo de colores.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

todos_bajos = np.array([20,50,50])
todos_altos = np.array([180,255,255])

mask_todos = cv2.inRange(hsv, todos_bajos, todos_altos)

cv2.imshow('Original', img)
cv2.imshow('Rojo+Fucsia+Azul+Verde+Amarillo', mask_todos)
print('\nPulsa cualquier tecla para cerrar las ventanas\n')
cv2.waitKey(0)
cv2.destroyAllWindows()
