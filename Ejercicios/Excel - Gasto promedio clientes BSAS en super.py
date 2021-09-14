# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:55:30 2021

@author: Nico
"""

import openpyxl
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

provincia=Excelsheet['B']
gasto_super=Excelsheet['D']
cant_clientes=0
gasto_prom_clientes_ba=0

indice=0

for celda in gasto_super:
    if indice>0:
        if provincia[indice].value=="Buenos Aires":
            cant_clientes=cant_clientes+1
            gasto_prom_clientes_ba=gasto_prom_clientes_ba+float(celda.value)
            
    indice=indice+1

gasto_prom_clientes_ba=gasto_prom_clientes_ba/cant_clientes

print("EL GASTO PROMEDIO EN SUPER DE CLIENTES DE BSAS ES: ", gasto_prom_clientes_ba)

        