import cv2
import numpy as np
from tkinter import *
from tkinter.ttk import *
windows = Tk()
windows.title('¿Qué color quieres extraer?')
windows.geometry('350x200')
combo =Combobox(windows)
combo['value']=('Rojo','Celeste','Marron','Celeste, rojo y marron')
combo.current(0)
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
def clicked():
    (combo.get())
    cv2.imshow('foto original',img)
    if ((combo.get())=='Rojo'):
       cv2.imshow('Extraccion rojo',mask)
    if ((combo.get())=='Celeste'):
       cv2.imshow('Extraccion celeste',mask2)
    if ((combo.get())=='Marron'):
       cv2.imshow('Extraccion marron',mask3)
    if ((combo.get())=='Celeste, rojo y marron'):
       cv2.imshow('Extraccion marron, celeste y rojo',mask4) 
def cerrar():
    windows.destroy()
    exit()
btn=Button(windows,text='Enter', command= clicked)
btn1=Button(windows,text='Cerrar', command= cerrar)
combo.grid(column=0 , row=0)
btn.grid(column=4, row=0)
btn1.grid(column=5, row=0)
windows.mainloop()








