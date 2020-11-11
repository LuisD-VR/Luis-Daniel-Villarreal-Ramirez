
import matplotlib.pyplot as plt


Estados = ['Aguascalientes', 'Baja California', 'BCS', 'Suma']
Muertes = [614, 3557, 458, 4629]
color = ['blue', 'pink', 'orange', 'red']
 
fig, ax = plt.subplots()

ax.set_ylabel('Muertes')
ax.set_xlabel('Estados')
ax.set_title('Muertes de COVID por estado')
plt.bar(Estados, height=Muertes,color=color, width=1)


plt.show()


