import pyautogui as gui
import time


def coordenadas_pantalla():
    gui.mouseInfo() 

def automatizar_cargaformgoogle():
    
    #size de la pantalla, puede ser distinto de acuerdo a resolucion
    screenWidth, screenHeight = gui.size()
    
    #mover el mouse a x = 10 en la base de la altura de la pantalla
    #generalmente en Windows esta la barra de busqueda (Windows 10)
    gui.moveTo(10,screenHeight)
    gui.click()
    
    #buscar Firefox,debe estar instalado obviamente
    gui.typewrite('Firefox', interval=0.25)
    #abrirlo
    gui.press('enter')
    
    #demoramos la ejecucion para hacerlo mas natural y evitar errores
    #esperamos 2 segundos que abra el programa,experimentar con este valor ante errores
    time.sleep(2)
    
    #abrimos un tab nuevo en firefox y nos movemos a el
    gui.keyDown('alt')
    gui.press(' ')
    gui.press('x')
    gui.keyUp('alt')
    gui.click(250,22)
    gui.click(316,67)
    
    #Escribir en la barra de direccion el link al form 
    #Este es el link de MI form (Albert)
    #Si creaste uno tuyo cambiar a la direccion correcta por favor
    gui.typewrite('https://forms.gle/Uw5U5Fc8yoj9ojcG7')
    gui.press('enter')
    
    
    #esperar que cargue
    time.sleep(2)
    
    #==comenzar carga de form===
    #Recordar que estas son las instrucciones para MI form
    #Si usan el de ustedes tienen que cambiarlo como explicamos
    #de acuerdo al diseno que usen
    
    #Si,puedo asistir
    gui.click(510,601)
    
    #presionar tab para ir a la proxima seccion del formulario
    gui.press('tab', presses=2)
   
    
    #quienes asistiran?
    gui.typewrite('Nico Programmer')
    
    #presionar tab para ir a la proxima seccion del formulario
    gui.press('tab')
    
    #elijo curso data science
    gui.press('space')
    
    #presionar tab para ir a la proxima seccion del formulario
    gui.press('tab', presses=5)
    
    #escribir comentario
    gui.typewrite('Data Science en Python')
    
    #presionar tab para ir a la proxima seccion del formulario
    gui.press('tab')
    
    #envio el formulario
    gui.press('enter')
    
    #==fin carga de form===

##descomentar este para la demo de Google Forms
#automatizar_cargaformgoogle()

##descomentar este para mostrar el utilitario de coordenadas
coordenadas_pantalla()
