# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:27:22 2021

@author: la03237
"""

maximo_actual=0
mi_lista=[7,9,6,32,51,95,329,6215]

for numero in mi_lista:
    if numero>maximo_actual:
        maximo_actual=numero
        
print("EL MAXIMO ES: ", maximo_actual)

