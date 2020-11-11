from tkinter import *

def pulsar():
    print('Hola',estado.get())
    print(Confirmados.get())
    

ventana=Tk()
ventana.geometry('600x250')

etiqueta=Label(ventana,text='Estado:')
etiqueta.place(x=20,y=20)
etiqueta=Label(ventana,text='Confirmados:')
etiqueta.place(x=20,y=50)
etiqueta=Label(ventana,text='Defunciones:')
etiqueta.place(x=20,y=80)
etiqueta=Label(ventana,text='Recuperados:')
etiqueta.place(x=20,y=110)
etiqueta=Label(ventana,text='Activos:')
etiqueta.place(x=20,y=140)

boton=Button(ventana,text='Guardar',command=pulsar)
boton.place(x=50,y=180)

estado=StringVar()
cajatexto=Entry(ventana,textvariable=estado)
cajatexto.place(x=110,y=20)

Confirmados=IntVar()
cajatexto=Entry(ventana,textvariable=Confirmados)
cajatexto.place(x=110,y=50)

Defunciones=IntVar()
cajatexto=Entry(ventana,textvariable=Defunciones)
cajatexto.place(x=110,y=80)

Recuperados=IntVar()
cajatexto=Entry(ventana,textvariable=Recuperados)
cajatexto.place(x=110,y=110)

Activos=IntVar()
cajatexto=Entry(ventana,textvariable=Activos)
cajatexto.place(x=110,y=140)

ventana.mainloop()

