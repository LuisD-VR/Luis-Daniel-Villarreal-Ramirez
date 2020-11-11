from tkinter import *
from tkinter.ttk import*
import json

def lineaSearch(item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
         if my_list[position] == item:
             found = True
         position = position + 1
    return found

bolsa=['Aguascalientes','Baja California','Baja California Sur','Campeche',
       'Chiapas','Chihuahua','Coahuila','Colima','Durango','Guanajuato','Guerrero',
       'Hidalgo','Jalisco','Edo. México','Michoacan']

windows =Tk()
windows.title('Estados')

selected = IntVar()

rad1 = Radiobutton(windows,text='Aguascalientes     ',value=1,variable=selected)
rad2 = Radiobutton(windows,text='Baja California    ',value=2, variable=selected)
rad3 = Radiobutton(windows,text='B. California Sur  ',value=3, variable=selected)
rad4 = Radiobutton(windows,text='Campeche           ',value=4,variable=selected)
rad5 = Radiobutton(windows,text='Chiapas            ',value=5,variable=selected)
rad6 = Radiobutton(windows,text='Chihuahua          ',value=6,variable=selected)
rad7 = Radiobutton(windows,text='Coahuila           ',value=7,variable=selected)
rad8 = Radiobutton(windows,text='Colima             ',value=8,variable=selected)
rad9 = Radiobutton(windows,text='Durango            ',value=9,variable=selected)
rad10 = Radiobutton(windows,text='Guanajuato         ',value=10,variable=selected)
rad11 = Radiobutton(windows,text='Guerrero           ',value=11,variable=selected)
rad12 = Radiobutton(windows,text='Hidalgo            ',value=12,variable=selected)
rad13 = Radiobutton(windows,text='Jalisco            ',value=13,variable=selected)
rad14 = Radiobutton(windows,text='Edo. México        ',value=14,variable=selected)
rad15 = Radiobutton(windows,text='Michoacan          ',value=15,variable=selected)

def clicked():
    if(selected.get())==1:
        item=('Aguascalientes')
    if(selected.get())==2:
        item=('Baja California')
    if(selected.get())==3:
        item=('Baja California Sur')
    if(selected.get())==4:
        item=('Campeche')
    if(selected.get())==5:
        item=('Chiapas')
    if(selected.get())==6:
        item=('Chihuahua')
    if(selected.get())==7:
        item=('Coahuila')
    if(selected.get())==8:
        item=('Colima')
    if(selected.get())==9:
        item=('Durango')
    if(selected.get())==10:
        item=('Guanajuato')
    if(selected.get())==11:
        item=('Guerrero')
    if(selected.get())==12:
        item=('Hidalgo')
    if(selected.get())==13:
        item=('Jalisco')
    if(selected.get())==14:
        item=('Edo. México')
    if(selected.get())==15:
        item=('Michoacan')
    
    itemfound = lineaSearch(item,bolsa)
    if itemfound:
       data={}
       data['Aguascalientes']=[]
       data['Aguascalientes'].append({
        'Confirmados' : 7221,
        'Negativos' : 14363,
        'Sospechosos' : 297,
        'Defunciones' : 614,
        'Recuperados' :4969,
        'Activos' : 363,
        'Hospitalizados(%)' : 26.51,
        'Ambulatorios(%)' : 73.49})
 
       data['Baja California']=[]
       data['Baja California'].append({
        'Confirmados' : 19277,
        'Negativos' : 11821,
        'Sospechosos' : 1482,
        'Defunciones' : 3557,
        'Recuperados' : 12294,
        'Activos' : 299,
        'Hospitalizados(%)' : 34.01,
        'Ambulatorios(%)' : 65.99})

       data['Baja California Sur']=[]
       data['Baja California Sur'].append({
        'Confirmados' : 10185,
        'Negativos' : 13728,
        'Sospechosos' : 399,
        'Defunciones' : 458,
        'Recuperados' : 8316,
        'Activos' : 645,
        'Hospitalizados(%)' : 11.60,
        'Ambulatorios(%)' : 88.40})

       data['Campeche']=[]
       data['Campeche'].append({
        'Confirmados' : 5953,
        'Negativos' : 6919,
        'Sospechosos' : 140,
        'Defunciones' : 813,
        'Recuperados' : 4002,
        'Activos' : 43,
        'Hospitalizados(%)' : 31.18,
        'Ambulatorios(%)' : 68.82})

       data['Chiapas']=[]
       data['Chiapas'].append({
        'Confirmados' : 6534,
        'Negativos' : 5128,
        'Sospechosos' : 229,
        'Defunciones' : 1090,
        'Recuperados' : 4023,
        'Activos' : 52,
        'Hospitalizados(%)' : 36.62,
        'Ambulatorios(%)' : 68.38})

       data['Chihuahua']=[]
       data['Chihuahua'].append({
        'Confirmados' : 10988,
        'Negativos' : 10333,
        'Sospechosos' : 3634,
        'Defunciones' : 1377,
        'Recuperados' : 7324,
        'Activos' : 330,
        'Hospitalizados(%)' : 29.98,
        'Ambulatorios(%)' : 70.02})

       data['Coahuila']=[]
       data['Coahuila'].append({
        'Confirmados' : 26300,
        'Negativos' : 35405,
        'Sospechosos' : 3239,
        'Defunciones' : 1868,
        'Recuperados' : 21278,
        'Activos' : 1062,
        'Hospitalizados(%)' : 14.57,
        'Ambulatorios(%)' : 85.43})

       data['Colima']=[]
       data['Colima'].append({
        'Confirmados' : 4831,
        'Negativos' : 3356,
        'Sospechosos' : 218,
        'Defunciones' : 526,
        'Recuperados' : 3207,
        'Activos' : 298,
        'Hospitalizados(%)' : 27.94,
        'Ambulatorios(%)' : 72.06})

       data['Durango']=[]
       data['Durango'].append({
        'Confirmados' : 8854,
        'Negativos' : 15103,
        'Sospechosos' : 1472,
        'Defunciones' : 623,
        'Recuperados' : 6887,
        'Activos' : 581,
        'Hospitalizados(%)' : 14.93,
        'Ambulatorios(%)' : 85.07})

       data['Guanajuato']=[]
       data['Guanajuato'].append({
        'Confirmados' : 40645,
        'Negativos' : 55646,
        'Sospechosos' : 1970,
        'Defunciones' : 2894,
        'Recuperados' : 32543,
        'Activos' : 1323,
        'Hospitalizados(%)' : 15.43,
        'Ambulatorios(%)' : 84.57})

       data['Guerrero']=[]
       data['Guerrero'].append({
        'Confirmados' : 18816,
        'Negativos' : 12661,
        'Sospechosos' : 1200,
        'Defunciones' : 1938,
        'Recuperados' : 13980,
        'Activos' : 703,
        'Hospitalizados(%)' : 21.76,
        'Ambulatorios(%)' : 78.24})

       data['Hidalgo']=[]
       data['Hidalgo'].append({
        'Confirmados' : 12703,
        'Negativos' : 9205,
        'Sospechosos' : 342,
        'Defunciones' : 1936,
        'Recuperados' : 7704,
        'Activos' : 498,
        'Hospitalizados(%)' : 35.42,
        'Ambulatorios(%)' : 64.58})

       data['Jalisco']=[]
       data['Jalisco'].append({
        'Confirmados' : 26741,
        'Negativos' : 36374,
        'Sospechosos' : 2942,
        'Defunciones' : 3252,
        'Recuperados' : 17024,
        'Activos' : 1662,
        'Hospitalizados(%)' : 29.87,
        'Ambulatorios(%)' : 70.13})

       data['Edo. México']=[]
       data['Edo. México'].append({
        'Confirmados' : 80562,
        'Negativos' : 101310,
        'Sospechosos' : 22173,
        'Defunciones' : 11738,
        'Recuperados' : 47843,
        'Activos' : 1862,
        'Hospitalizados(%)' : 38.07,
        'Ambulatorios(%)' : 61.93})

       data['Michoacan']=[]
       data['Michoacan'].append({
        'Confirmados' : 20226,
        'Negativos' : 25975,
        'Sospechosos' : 2100,
        'Defunciones' : 1634,
        'Recuperados' : 15599,
        'Activos' : 652,
        'Hospitalizados(%)' : 19.18,
        'Ambulatorios(%)' : 80.82})
       
       for c in data[item]:
        print(item)
        print('Confirmados', c['Confirmados'])
        print('Negativos', c['Negativos'])
        print('Sospechosos', c['Sospechosos'])
        print('Defunciones', c['Defunciones'])
        print('Resuperados', c['Activos'])
        print('Hospitalizados', c['Hospitalizados(%)'],'%')
        print('Ambulatorios', c['Ambulatorios(%)'],'%')
        print('    ')

        with open('Datos COVID de '+item,'w') as file:
            json.dump(data[item],file)
        with open('Datos COVID de '+item) as file:
            data=json.load(file)

btn=Button(windows,text='Enter', command= clicked)

rad1.grid(column=0, row=0)
rad2.grid(column=0, row=1)
rad3.grid(column=0, row=2)
rad4.grid(column=0, row=3)
rad5.grid(column=1, row=4)
rad6.grid(column=1, row=0)
rad7.grid(column=1, row=1)
rad8.grid(column=1, row=2)
rad9.grid(column=1, row=3)
rad10.grid(column=2, row=4)
rad11.grid(column=2, row=0)
rad12.grid(column=2, row=1)
rad13.grid(column=2, row=2)
rad14.grid(column=2, row=3)
rad15.grid(column=3, row=4)

btn.grid(column=5, row=0)


windows.mainloop()
