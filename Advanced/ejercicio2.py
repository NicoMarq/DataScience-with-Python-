import pandas as pd

#Ejercicio con un Excel que tiene una tabla de datos
#Pero tambien tiene un mensaje en las primeras filas que molestan
#Tambien el que envio el informe , le saco los titulos
#Debemos ponerlos nosotros mismos


#Abro el Excel y ya me lo devuelve en un dataframe
#Para colocar los titulos manualmente utilizamos UNA LISTA
#Utilizamos el Skiprows para que no tome las filas que tiene el mensaje
excelclientes_df = pd.read_excel("C:/MuestraTarjetaX2019_archivomalo1.xlsx", header=None,
                                 names=["DNI", "LUGAR", "SUELDO", "AÑOS", "GENERO", "Hola", "chau", "pepino", "azucar", "lenteja", "arroz", "cebolla", "salsa", "adios", "bien", "che", "Nicolas", "pepe", "sergio", "asies", "claudia", "agos", "mary"], skiprows=9)


print(excelclientes_df.info()) #Con esta funcion le pido los datos estadisticos principales
print(excelclientes_df.head(5)) #Aqui le pido solo las primeras 5 lineas a modo de explorar

