# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:50:58 2021

@author: Nico
"""

import openpyxl
Excelworkbook=openpyxl.load_workbook('C:/MuestraTarjetaX2019.xlsx')
Excelsheet=Excelworkbook.active

celda_h11=Excelsheet['H11'].value
print(celda_h11)
    
    

