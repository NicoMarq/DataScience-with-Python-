# -*- coding: utf-8 -*-
"""
Created on Sun May 23 12:05:51 2021

@author: Nico
"""

#IMPORTAMOS LIBRERIA Y ARCHIVO

import openpyxl
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

#PROMEDIO INGRESOS CLIENTE

#DEFINO LA VARIABLE PROMEDIO INGRESOS

promedio_ingresos_clientes=0

#DEFINO EL LOOP PARA RECORRER EL RANGO DE INGRESOS


for fila in Excelsheet.iter_rows(min_row=1,max_row=3,values_only=True):
    print(fila)
    
    
    
    


