import pandas as pd

#Creo un dataset
mis_empleados = pd.DataFrame({"nombre": ["Nico", "Estefi", "Jorge", "Pedro", "Jesica", "Hector"], 
                              "edad":[33, 44, 29, 45, 37, 28], 
                              "sueldo":[40000, 66000, 102222, 32089, 342132, 234343]})

#Agrego una columna con el nuevo sueldo actualizado
#Utilizo la funcion apply y defino la funcion lambda

mis_empleados["Sueldo Actualizado"] = mis_empleados.apply(lambda x: x["sueldo"]*1.2, axis=1)

print(mis_empleados)

