# -*- coding: utf-8 -*-
"""
Created on Sat May 22 22:11:23 2021

@author: Nico
"""

#DEFINO VALOR DE SMA200
sma200=13000

#DEFINO LISTA DE PRECIOS DE CIERRE DE ACTIVO

precios_cierre=[32323,3424,1324242,123123,122]

#DEFINO EL LOOP Y LA CONDICION

for precio in precios_cierre:
    if precio<sma200:
        print(precio,"SELL")
    else:
        print(precio,"BUY")
        
        
    
    