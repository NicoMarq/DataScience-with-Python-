# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:19:06 2021

@author: la03237
"""
#Defino las variables de peso muñeca y peso payaso
pesopayaso = 112
pesomuñeca = 75


cantpayasos = 0
cantmuñecas = 0

print ("HOLA JUGUETERIA")

cantmuñecas = int(input("INGRESE CANTIDAD DE MUÑECAS EN ULTIMO PEDIDO: "))
cantpayasos = int(input("INGRESE CANTIDAD DE PAYASOS EN ULTIMO PEDIDO: "))

pesopedido = (pesomuñeca * cantmuñecas) + (pesopayaso * cantpayasos)

print ("EL PESO TOTAL DEL PEDIDO ES: " , pesopedido)




