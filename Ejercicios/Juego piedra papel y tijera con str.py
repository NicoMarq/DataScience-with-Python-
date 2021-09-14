# -*- coding: utf-8 -*-
"""
Created on Sat May 22 19:15:17 2021

@author: Nico
"""

print("JUGAMOS PIEDRA, PAPEL , TIJERA?")

jugador1=str(input("JUEGA JUGADOR 1: "))
jugador2=str(input("JUEGA JUGADOR 2: "))

if jugador1==("PAPEL") and jugador2==("PAPEL"):
    print("EMPATE")
    
if jugador1==("PAPEL") and jugador2==("PIEDRA"):
        print("GANA JUGADOR 1")
        
if jugador1==("PAPEL") and jugador2==("TIJERA"):
        print("GANA JUGADOR2")
        
if jugador1==("TIJERA") and jugador2==("PAPEL"):
        print("GANA JUGADOR 1")
        
if jugador1==("TIJERA") and jugador2==("PIEDRA"):
        print("GANA JUGADOR 2")
        
if jugador1==("TIJERA") and jugador2==("TIJERA"):
        print("EMPATE")
        

    
