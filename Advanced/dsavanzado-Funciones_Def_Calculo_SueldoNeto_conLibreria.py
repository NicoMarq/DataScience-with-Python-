import pandas as pd
import liquidacion_sueldo_lib as liqargy

#Creo un dataset
mis_empleados = pd.DataFrame({"nombre": ["Nico", "Estefi", "Jorge", "Pedro", "Jesica", "Hector"], 
                              "edad":[33, 44, 29, 45, 37, 28], 
                              "sueldo_bruto":[40000, 66000, 102222, 32089, 342132, 234343]})

#uso apply para aplicar la funcion que cree mas arriba a cada celda de la columna sueldo del dataframe
#el resultado se guardara en una nueva columna sueldo neto
mis_empleados["sueldo_neto"]=mis_empleados["sueldo_bruto"].apply(liqargy.calculo_sueldoneto)

print(mis_empleados)

