# -*- coding: utf-8 -*-
"""
Created on Sat May 22 19:44:14 2021

@author: Nico
"""

#MAXIMO NUMERO EN UNA LISTA PROPIA

numero_actual=0
mi_lista=[3,4,213,453,23,534,534354363415]

for numero in mi_lista:
    if numero>numero_actual:
        numero_actual=numero
        
print("EL MAXIMO NUMERO ES: ", numero_actual)

