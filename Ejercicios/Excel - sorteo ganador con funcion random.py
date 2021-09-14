# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:00:25 2021

@author: Nico
"""

#GANADOR PRECIO POR LOS ID

import openpyxl
import random
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

#CANTIDAD DE CLIENTES/FILAS

cantidad_clientes=Excelsheet.max_row

#DEFINO VARIABLE DE ID Y LE DIGO QUE ESO ESTÁ EN LA COLUMNA A
id_Clientes=Excelsheet['A']

#DEFINO VARIABLE GANADOR CON FUNCION RANDOM
#ENTRE LA MATRIZ 1 (SIN EL TITULO) Y CANT CLIENTES
#LE ESPECIFICO QUE ME TRAIGA EL VALOR DE LA CELDA GANADOR QUE SALGA SORTEADA
ganador=random.randrange(1, cantidad_clientes)
ganador=int(ganador)

print("ID Cliente ganador: ", id_Clientes[ganador].value)



