import cv2
import numpy as np

img = cv2.imread('img.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rojo_bajos = np.array([0,100,100])
rojo_altos = np.array([10,255,255])
celeste_bajos = np.array([75,100,100])
celeste_altos = np.array([95,255,255])
marron_bajos = np.array([170,100,100])
marron_altos = np.array([180,255,255])
mask = cv2.inRange(hsv,rojo_bajos,rojo_altos)
mask2 = cv2.inRange(hsv,celeste_bajos,celeste_altos)
mask3 = cv2.inRange(hsv,marron_bajos,marron_altos)
mask4 = mask+mask2+mask3
cv2.imshow('foto original',img)

cv2.imshow('Extraccion rojo',mask)
cv2.imshow('Extraccion celeste',mask2)
cv2.imshow('Extraccion marron',mask3)
cv2.imshow('Extraccion marron, celeste y rojo',mask4) 
cv2.waitKey(0)
                       
cv2.destroyALLWindows()
