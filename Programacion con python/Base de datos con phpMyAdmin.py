import mysql.connector
from tkinter import *
from tkinter.ttk import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="covid estados"
)
windows = Tk()
def menu():
 windows.destroy()
 windows.__init__()
 windows.title('¿Qué quieres hacer?')
 windows.geometry('600x250')
 mycursor = mydb.cursor()
 
 def cerrar():
     windows.destroy()
 def agg():
     windows.destroy()
     windows.__init__()
     def guardar():
          mycursor.execute("SELECT MAX(Control) AS maximum FROM estados")
          result = mycursor.fetchall()
          for i in result:
               x=i[0]
          x=x+1
          sql=("""INSERT INTO estados (Control, Estado) VALUES (%s,%s)""")
          val= (x,Estado.get())
          sqll = ("""INSERT INTO datos (ControlD, Confirmados, Defunciones,
          Recuperados, Activos) VALUES (%s,%s,%s,%s,%s) """)
          vall = (x,Confirmados.get(),Defunciones.get(),Recuperados.get(),Activos.get())
          mycursor.execute(sql, val)
          mycursor.execute(sqll, vall)
          mydb.commit()
          windows.destroy()
          windows.__init__()
          windows.title('Agregar')
          windows.geometry('600x250')
          eti=Label(windows, text='Se guardo correctamente')
          eti.place(x=220,y=20)
          boton=Button(windows,text='Menu',command=menu)
          boton.place(x=250,y=140)
          boton=Button(windows,text='Cerrar',command=cerrar)
          boton.place(x=250,y=180)
          
     windows.title('Agregar')
     windows.geometry('600x250')

     etiqueta=Label(windows,text='Estado:')
     etiqueta.place(x=20,y=20)
     etiqueta=Label(windows,text='Confirmados:')
     etiqueta.place(x=20,y=50)
     etiqueta=Label(windows,text='Defunciones:')
     etiqueta.place(x=20,y=80)
     etiqueta=Label(windows,text='Recuperados:')
     etiqueta.place(x=20,y=110)
     etiqueta=Label(windows,text='Activos:')
     etiqueta.place(x=20,y=140)

     Estado=StringVar()
     cajatexto=Entry(windows,textvariable=Estado)
     cajatexto.place(x=110,y=20)
     Confirmados=IntVar()
     cajatexto=Entry(windows,textvariable=Confirmados)
     cajatexto.place(x=110,y=50)
     Defunciones=IntVar()
     cajatexto=Entry(windows,textvariable=Defunciones)
     cajatexto.place(x=110,y=80)
     Recuperados=IntVar()
     cajatexto=Entry(windows,textvariable=Recuperados)
     cajatexto.place(x=110,y=110)
     Activos=IntVar()
     cajatexto=Entry(windows,textvariable=Activos)
     cajatexto.place(x=110,y=140)
     boton=Button(windows,text='Guardar',command=guardar)
     boton.place(x=50,y=180)

 def consultar():
    windows.destroy()
    windows.__init__()
    windows.title('Consulta')
    windows.geometry('600x250')
    combo =Combobox(windows)
    mycursor.execute("SELECT Estado FROM estados")
    myresult = mycursor.fetchall()
    a= [""]
    w=0
    for w in myresult:
        a.append(w)

    a = tuple(a)
    combo['value']=tuple(a)
    combo.current(0)

    def clicked():
        mycursor.execute("SELECT Control FROM estados WHERE Estado = %(nom)s;",{"nom":combo.get()})
        mresult = mycursor.fetchall()
        x=mresult[0][0]
        mycursor.execute("SELECT * FROM datos WHERE ControlD = %(num)s;",{"num":x})
        myresult = mycursor.fetchall()
        a=myresult[0][0]
        b=myresult[0][1]
        c=myresult[0][2]
        d=myresult[0][3]
        e=myresult[0][4]
        f=combo.get()
        windows.destroy()
        windows.__init__()
        windows.geometry('600x250')
        windows.title('Consultar')
        windows.geometry('600x250')
        et=Label(windows, text=f)
        et.place(x=250, y=20)
        eti=Label(windows, text='Control          Confirmados        Defunciones         Recuperados           Activos')
        eti.place(x=100,y=50)
        et=Label(windows, text=a)
        et.place(x=115, y=70)
        et=Label(windows, text=b)
        et.place(x=190, y=70)
        et=Label(windows, text=c)
        et.place(x=285, y=70)
        et=Label(windows, text=d)
        et.place(x=375, y=70)
        et=Label(windows, text=e)
        et.place(x=470, y=70)
        boton=Button(windows,text='Menu',command=menu)
        boton.place(x=250,y=140)
        boton=Button(windows,text='Cerrar',command=cerrar)
        boton.place(x=250,y=180)
        
    btn=Button(windows,text='Enter', command= clicked)
    btn1=Button(windows,text='Cerrar', command=cerrar)
    combo.grid(column=0 , row=0)
    btn.grid(column=3, row=0)
    btn1.grid(column=3,row=2)

 def eliminar():
    windows.destroy()
    windows.__init__()
    windows.title('Eliminar')
    windows.geometry('600x250')
    combo =Combobox(windows)
    mycursor.execute("SELECT Estado FROM estados")
    myresult = mycursor.fetchall()
    a= [""]
    for w in myresult:   
        a.append(w)

    a = tuple(a)
    combo['value']=tuple(a)
    combo.current(0)
    
    def elm():
        mycursor.execute("SELECT Control FROM estados WHERE Estado = %(nom)s;",{"nom":combo.get()})
        mresult = mycursor.fetchall()
        x=mresult[0][0]
        mycursor.execute("DELETE FROM datos WHERE ControlD = %(num)s;",{"num":x})
        mycursor.execute("DELETE FROM estados WHERE Control = %(num)s;",{"num":x})
        mydb.commit()
        windows.destroy()
        windows.__init__()
        windows.title('Agregar')
        windows.geometry('600x250')
        eti=Label(windows, text='Se elimino correctamente')
        eti.place(x=220,y=20)
        boton=Button(windows,text='Menu',command=menu)
        boton.place(x=250,y=140)
        boton=Button(windows,text='Cerrar',command=cerrar)
        boton.place(x=250,y=180)
        
    btn=Button(windows,text='Enter', command= elm)
    btn1=Button(windows,text='Cerrar', command=windows.destroy)
    combo.grid(column=0 , row=0)
    btn.grid(column=3, row=0)
    btn1.grid(column=3,row=2)

 def Actualizar():
    windows.destroy()
    windows.__init__()
    windows.title('Actualizar')
    windows.geometry('600x250')
    combo =Combobox(windows)
    mycursor.execute("SELECT Estado FROM estados")
    myresult = mycursor.fetchall()
    a= [""]
    for w in myresult:   
        a.append(w)

    a = tuple(a)
    combo['value']=tuple(a)
    combo.current(0)
    def up():
        windows.title('Actualizar')
        windows.geometry('600x250')
        def cambiar():
             cursor = mydb.cursor()
             cursor.execute("SELECT Control FROM estados WHERE Estado = %(nom)s;",{"nom":combo.get()})
             mresult = cursor.fetchall()
             x=mresult[0][0]
             mycursor = mydb.cursor()
            
             sql = "UPDATE datos SET Confirmados = %s WHERE ControlD = %s"
             val = (Confirmados.get(), x) 
             mycursor.execute(sql,val)
             sql2 = "UPDATE datos SET Defunciones = %s WHERE ControlD = %s"
             val2 = (Defunciones.get(), x) 
             mycursor.execute(sql2,val2)
             sql3 = "UPDATE datos SET Recuperados = %s WHERE ControlD = %s"
             val3 = (Recuperados.get(), x) 
             mycursor.execute(sql3,val3)
             sql4 = "UPDATE datos SET Activos = %s WHERE ControlD = %s"
             val4 = (Activos.get(), x) 
             mycursor.execute(sql4,val4)
             mydb.commit()
             windows.destroy()
             windows.__init__()
             windows.title('Agregar')
             windows.geometry('600x250')
             eti=Label(windows, text='Se actualizo la informacion correctamente')
             eti.place(x=150,y=20)
             boton=Button(windows,text='Menu',command=menu)
             boton.place(x=250,y=140)
             boton=Button(windows,text='Cerrar',command=cerrar)
             boton.place(x=250,y=180)
        
        etiqueta=Label(windows,text='Estado: ' + combo.get())
        etiqueta.place(x=300,y=30)
        etiqueta=Label(windows,text='Confirmados:')
        etiqueta.place(x=300,y=60)
        etiqueta=Label(windows,text='Defunciones:')
        etiqueta.place(x=300,y=90)
        etiqueta=Label(windows,text='Recuperados:')
        etiqueta.place(x=300,y=120)
        etiqueta=Label(windows,text='Activos:')
        etiqueta.place(x=300,y=150)

        Confirmados=IntVar()
        cajatexto=Entry(windows,textvariable=Confirmados)
        cajatexto.place(x=390,y=60)
        Defunciones=IntVar()
        cajatexto=Entry(windows,textvariable=Defunciones)
        cajatexto.place(x=390,y=90)
        Recuperados=IntVar()
        cajatexto=Entry(windows,textvariable=Recuperados)
        cajatexto.place(x=390,y=120)
        Activos=IntVar()
        cajatexto=Entry(windows,textvariable=Activos)
        cajatexto.place(x=390,y=150)
        boton=Button(windows,text='Guardar cambios',command=cambiar)
        boton.place(x=340,y=180)
        
    btn=Button(windows,text='Enter', command= up)
    btn1=Button(windows,text='Cerrar', command=windows.destroy)
    combo.grid(column=0 , row=0)
    btn.grid(column=3, row=0)
    btn1.grid(column=3,row=2)

 boton=Button(windows,text='Consultar ',command=consultar)
 boton.place(x=10,y=10)
 boton1=Button(windows,text='Agregar Estado ',command=agg )
 boton1.place(x=10,y=50)
 boton2=Button(windows,text='Eliminar Estado ',command=eliminar)
 boton2.place(x=10,y=90)
 boton3=Button(windows,text='Actualizar Estado ',command=Actualizar)
 boton3.place(x=10,y=130)
 boton4=Button(windows,text='Cerrar', command=cerrar)
 boton4.place(x=10,y=170)
 windows.mainloop()
menu()


