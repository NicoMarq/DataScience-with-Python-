# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:19:41 2021

@author: Nico
"""

import matplotlib.pyplot as plt
import pandas as pd

#Leo archivo csv
ggal=pd.read_csv('C:/Users/Nico/Documents/Cursos/Data Science/Basico/GGAL.csv')

#Defino Figure y le modifico el tamaño con figsize(anchoxalto)
fig1 = plt.figure(figsize=(20,15))

#Defino Axes
ax = fig1.subplots()

#Defino la serie de datos a tomar por el plot
#Le defino propiedades de diseño a la linea graficada
plt.plot(ggal['Date'], ggal['Adj Close'], color='#C62C1D', lw=2.5, marker='.')

#Guardamos los axes en una variable para luego rotarlos
xlabels=ax.get_xticklabels()
plt.setp(xlabels, rotation=90)


#Le digo al eje Y que comience desde 0 hasta 18
plt.ylim(0,18)
plt.xlim('2020-01-01','2021-06-02')



#Le coloco los bordes ausentes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#Le agrego una grilla
ax.yaxis.grid(color='black', linestyle='dashed', alpha=1)
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

#Titulos de ejes
plt.ylabel('Precio en USD')
plt.xlabel('2021 WTD')

#Titulos y subtitulos del grafico
plt.title('Precio Accion GGAL en USD', loc='left', fontsize=14)
fig1.suptitle('COTIZACION ACCION GRUPO FINANCIERO GALICIA EN USD', x=0.125, y=0.91, ha='left', fontsize=18)
                             
#Muestro grafico
plt.show()

    