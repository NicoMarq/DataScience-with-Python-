# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:19:21 2021

@author: Nico
"""

import openpyxl
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

cant_clientes_no_viven_ba=0
provincia=Excelsheet['B']

indice=0

for celda in provincia:
    if indice>0:
        if provincia[indice].value!="Buenos Aires":
            cant_clientes_no_viven_ba=cant_clientes_no_viven_ba+1
            
    indice=indice+1
    
print("CANTIDAD DE CLIENTES QUE NO VIVEN EN BUENOS AIRES: ",cant_clientes_no_viven_ba)

