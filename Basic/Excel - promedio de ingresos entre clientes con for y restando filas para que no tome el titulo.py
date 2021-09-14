# -*- coding: utf-8 -*-
"""
Created on Sun May 23 12:19:13 2021

@author: Nico
"""

#IMPORTAMOS LIBRERIA Y ARCHIVO

import openpyxl
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

#PROMEDIO INGRESOS CLIENTES
#DEFINO VARIABLE DE PROMEDIO Y LA COLUMNA INGRESOS

promedio_ingresos_cliente=0
ingresos_cliente=Excelsheet['C']

#DEFINO VARIABLE PARA SALTEAR EL TITULO
fila_actual=1


#DEFINO EL LOOP PARA RECORRER LA COLUMNA INGRESOS
#COLOCO EL CASTING PARA LA CELDA.VALUE PARA NUMEROS CON DECIMALES
#DENTRO DEL LOOP COLOCO UN CONDICIONAL IF PARA SABER ASEGURAR QUE NO TOME EL TITULO
#AL FINAL COLOCO EL CONTADOR

for celda in ingresos_cliente:
    if fila_actual>1:
            promedio_ingresos_cliente=promedio_ingresos_cliente+float(celda.value)
            
    fila_actual=fila_actual+1

#RESTAMOS DOS FILAS AL CONTADOR PORQUE ES LA DEL TITULO
    
fila_actual=fila_actual-2

print("EL PROMEDIO DE INGRESOS DE LOS CLIENTES ES: ", promedio_ingresos_cliente/fila_actual)

