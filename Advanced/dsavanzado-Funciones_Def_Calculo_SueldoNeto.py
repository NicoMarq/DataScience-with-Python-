#Vamos a calcular el sueldo neto de una lista de empleados, 
#partiendo del sueldo Bruto

import pandas as pd

#Creamos las variables de los descuentos
descuento_jubilacion = 0.11
descuento_obrasocial = 0.20
descuento_cuotasindical = 0.03
descuento_ganancias = 0.35


#Defino la funcion
def calculo_sueldoneto(sueldo_bruto):
    sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_jubilacion)
    sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_obrasocial)
    sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_cuotasindical)
    
    if (sueldo_bruto>=100000):
        sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_jubilacion)
        
    return sueldo_neto



#Creo un dataset
mis_empleados = pd.DataFrame({"nombre": ["Nico", "Estefi", "Jorge", "Pedro", "Jesica", "Hector"], 
                              "edad":[33, 44, 29, 45, 37, 28], 
                              "sueldo_bruto":[40000, 66000, 102222, 32089, 342132, 234343]})


#uso apply para aplicar la funcion que cree mas arriba a cada celda de la columna sueldo del dataframe
#el resultado se guardara en una nueva columna sueldo neto
mis_empleados["sueldo_neto"]=mis_empleados["sueldo_bruto"].apply(calculo_sueldoneto)

print(mis_empleados)