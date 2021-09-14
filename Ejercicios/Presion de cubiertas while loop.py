# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:49:55 2021

@author: la03237
"""

barometro=0
while (barometro!=30):
        
        barometro=int(input("INGRESE AIRE: "))
        
        if(barometro==30):
            print("OK AIRE PRESION")
        
        else:
            print("AIRE NOK")
            
            if (barometro>30):
                print("DESINFLE")
            
            if (barometro<30):
                print("INFLE")
                
                