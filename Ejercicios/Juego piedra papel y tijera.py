# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:27:22 2021

@author: la03237
"""

print("¡COMIENZA EL JUEGO!")

nico=input("Nico elige: ")
pc=input("PC elije: ")


if nico==pc:
    print("EMPATE")

if (nico=="PAPEL" and pc=="TIJERA"):
    print("TIJERA CORTA A PAPEL, GANA LA PC")
    
if (nico=="PAPEL" and pc=="PIEDRA"):
    print("PAPEL ENVUELVE A PIEDRA, GANA NICO")
    
if (nico=="TIJERA" and pc=="PIEDRA"):
    print("PIEDRA ROMPE A TIJERA, GANA PC")
    
if (nico=="TIJERA" and pc=="PAPEL"):
    print("TIJERA CORTA PAPEL , GANA NICO")
    
if (nico=="PIEDRA" and pc=="TIJERA"):
    print("PIEDRA ROMPE TIJERA, GANA NICO")
    
if (nico=="PIEDRA" and pc=="PAPEL"):
    print("PAPEL ENVUELVE PIEDRA, GANA PC")

    
    

