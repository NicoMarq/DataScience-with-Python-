# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:11:18 2021

@author: Nico
"""

import openpyxl
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

estado_civil=Excelsheet['W']
ingresos=Excelsheet['C']
cant_solteros=0
cant_casados=0
gasto_prom_solteros=0
gasto_prom_casados=0
indice=0

for celda in ingresos:
    if indice>0:
        if estado_civil[indice].value=="Soltero":
            cant_solteros=cant_solteros+1
            gasto_prom_solteros=gasto_prom_solteros+float(celda.value)
        
        if estado_civil[indice].value=="Casado":
            cant_casados=cant_casados+1
            gasto_prom_casados=gasto_prom_casados+float(celda.value)
            
    indice=indice+1
    
gasto_prom_solteros=gasto_prom_solteros/cant_solteros
gasto_prom_casados=gasto_prom_casados/cant_casados

if gasto_prom_solteros==gasto_prom_casados:
    print("LOS DOS GANAN IGUAL EN PROMEDIO")
    
else:
    print("EN PROMEDIO GANAN MAS LOS: ")
    
    if gasto_prom_solteros<gasto_prom_casados:
        print("CASADOS ; GANAN EN PROMEDIO: ", gasto_prom_casados)
        
    if gasto_prom_solteros>gasto_prom_casados:
        print("SOLTEROS ; GANAN EN PROMEDIO: ",gasto_prom_solteros)
        
        

       
    
    
    
    
    
    