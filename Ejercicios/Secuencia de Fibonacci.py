# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 18:11:27 2021

@author: la03237
"""

#Defino cuantos numeros quiero que tenga la serie
cuantosnumerosquiero = 100

#Defino las variables para la formula. Al principio serán 2: 0 y 1
numero1 = 0
numero2 = 1

#Defino variable la cual contendrá el resultado de la suma para cada par de numeros
numeron = 0

#Defino cuantos numeros voy
cuantosnumerosvoy = 0

#Titulo
print ("SECUENCIA DE FIBONACCI POR NICO")

#Ahora a hacer la loop hasta llegar a los 100 numeros de la serie
while (cuantosnumerosvoy < cuantosnumerosquiero):
    print (numero1)
    numeron = numero1 + numero2
    #Actualizo para que siempre el resultado sea la suma de los ultimos 2 numeros
    numero1 = numero2
    numero2 = numeron
    
    #Actualizo mi cuenta
    cuantosnumerosvoy += 1
    
    
