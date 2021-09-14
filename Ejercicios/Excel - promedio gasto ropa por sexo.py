# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:39:00 2021

@author: Nico
"""

import openpyxl
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

#PROMEDIO GASTO INDUMENTARIA POR SEXO

#DEFINO VARIABLES PROMEDIO PARA CADA SEXO 
#DEFINO VARIABLES DE LAS COLUMNAS INDUMENTARIA Y SEXO
#DEFINO VARIABLES DEL CONTADOR DE CANT HOMBRES Y MUJERES
gasto_prom_ropa_hombres=0
gasto_prom_ropa_mujeres=0
gasto_indumentaria=Excelsheet['H']
sexo_cliente=Excelsheet['V']
cant_hombres=0
cant_mujeres=0


#DEFINO VARIABLE INDICE PARA UBICARME EN LAS COLUMNAS

indice=0

#COMIENZO CON EL LOOP
#POR CADA CELDA EN GASTO INDUMENTARIA
#ASEGURAMOS QUE EL INDICE SEA MAYOR A 0 PARA QUE NO INCLUYA EL TITULO
#CONDICIONAL, SI EN LA CELDA DICE MASCULINO QUE CUENTE PARA EL Y VAYA SUMANDO
#LO MISMO EL CONDICIONAL PARA MUJERES

for celda in gasto_indumentaria:
    if indice>0:
        if sexo_cliente[indice].value=="Masculino":
            cant_hombres=cant_hombres+1
            gasto_prom_ropa_hombres=gasto_prom_ropa_hombres+float(celda.value)
        elif sexo_cliente[indice].value=="Femenino":
            cant_mujeres=cant_mujeres+1
            gasto_prom_ropa_mujeres=gasto_prom_ropa_mujeres+float(celda.value)
            
    indice=indice+1
    
#DEFINO LAS FORMULAS DEL PROMEDIO PARA CADA SEXO
gasto_prom_ropa_hombres=gasto_prom_ropa_hombres/cant_hombres
gasto_prom_ropa_mujeres=gasto_prom_ropa_mujeres/cant_mujeres
    
print("EL PROMEDIO DE GASTO EN ROPA EN HOMBRES ES: ",gasto_prom_ropa_hombres)
print("EL PROMEDIO DE GASTO EN ROPA EN MUJERES ES: ",gasto_prom_ropa_mujeres)
