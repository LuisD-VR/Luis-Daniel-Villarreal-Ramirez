import cv2
import tkinter
import Image , ImageTk

camara = cv2.VideoCapture(0)
a=1
while a==1:
   leido,frame=camara.read()

   if leido == True:
       def c():
          root.destroy()
          exit()
   
       cv2.imwrite('foto.png',frame)
       imagenAnchuraMaxima=1000
       imagenAlturaMaxima=500

       img = Image.open('foto.png')

       img.thumbnail((1000,500), Image.ANTIALIAS)

       root=tkinter.Tk()
       root.title('mostrar imagen')
       tkimage=ImageTk.PhotoImage(img)
       label=tkinter.Label(root, image=tkimage, width=1000,height=500).pack()
       buttonStart1=tkinter.Button(root, text='Cerrar',command=c).pack()
       buttonStart2=tkinter.Button(root, text='Otra foto',command=root.destroy).pack()
       root.mainloop()
    
   else:
    print('Error camara no existente, apagada o no configurada')
 
camara.release()
