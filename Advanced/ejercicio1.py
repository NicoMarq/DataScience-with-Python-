import pandas as pd

#Ejercicio con un Excel que tiene una tabla de datos
#Pero tambien tiene un mensaje en las primeras filas que molestan


#Abro el Excel y ya me lo devuelve en un dataframe
#Para que la lectura en Python no tome las lineas con el mensaje aplicamos:
excelclientes_df = pd.read_excel("C:/MuestraTarjetaX2019_archivomalo1.xlsx", header=[8])


print(excelclientes_df.info()) #Con esta funcion le pido los datos estadisticos principales
print(excelclientes_df.head(5)) #Aqui le pido solo las primeras 5 lineas a modo de explorar




