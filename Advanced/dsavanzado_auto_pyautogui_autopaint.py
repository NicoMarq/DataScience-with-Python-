import pyautogui

#size de la pantalla, puede ser distinto de acuerdo a resolucion
screenWidth, screenHeight = pyautogui.size()
    
#mover el mouse a x = 10 en la base de la altura de la pantalla
#generalmente en Windows esta la barra de busqueda (Windows 10)
pyautogui.moveTo(10,screenHeight)
pyautogui.click()
    
#buscar Paint 
pyautogui.typewrite('Paint', interval=0.25)

#abrirlo
pyautogui.press('enter')
    
#esperamos 3 segundos que abra el programa,experimentar con este valor ante errores
pyautogui.sleep(3)

#seleccionar lapiz
pyautogui.click(244,68)

#seleccionar canvas
pyautogui.click(58,231)

#dibujo 
distancia = 300
cambio = 20

while distancia > 0:
    pyautogui.drag(distancia, 0, duration=0.2)   # arrastrar el mouse esa distancia y duracion
    distancia = distancia - cambio
    pyautogui.drag(0, distancia, duration=0.2)   # arrastrar hacia abajo
    pyautogui.drag(-distancia, 0, duration=0.2)  # arrastrar hacia arriba
    distancia = distancia - cambio
    pyautogui.drag(0, -distancia, duration=0.2)  # hacia arriba
    
