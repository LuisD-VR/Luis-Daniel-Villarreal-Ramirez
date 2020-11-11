#Extraer color rojo, amarillo y azul
import cv2
import numpy as np

captura = cv2.VideoCapture(0)
 
while(1):
     
    
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 

    rojo_bajos = np.array([170,140,70], dtype=np.uint8)
    rojo_altos = np.array([180, 255, 240], dtype=np.uint8)
    amarillo_bajos = np.array([0,100,70], dtype=np.uint8)
    amarillo_altos = np.array([40, 255, 240], dtype=np.uint8)
    azul_bajos = np.array([100,140,70], dtype=np.uint8)
    azul_altos = np.array([130, 255, 240], dtype=np.uint8)
   
    mask = cv2.inRange(hsv, rojo_bajos, rojo_altos)
    mask1 = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
    mask2 = cv2.inRange(hsv, azul_bajos, azul_altos)
    maskT = mask + mask1 + mask2
 
    moments = cv2.moments(maskT)
    area = moments['m00']
 
    if(area > 2000000):
         
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        print ("x = ", x)
        print ("y = ", y)
 
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
     
    cv2.imshow('mask', maskT)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()

