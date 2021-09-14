import pandas as pd

#Importamos el Excel usando Openpyxl y le decimos que los titulos estan
#en la primera fila del Excel
#read_excel nos devuelve un dataframe con todos los datos

excel_clientes_df = pd.read_excel("C:/MuestraTarjetaX2019.xlsx", header=[0], engine="openpyxl")

#Creamos variable para establecer rango de salario para Premium
ingresomin_black = 550000

#Exportamos a un excel nuevo
#Guardo el archivo nuevo
writer=pd.ExcelWriter("I:/DataScience/AnalisisBanco.xlsx")

#Filtramos el dataframe inicial por Ingresos y almacenamos en un nuevo dataframe
#Usamos method chaining para escirbir el datafram en la hoja
#Usamos to_excel para escribirlo en un excel nuevo con luego el write
clientes_black_df = excel_clientes_df[excel_clientes_df["INGRESOS"]>ingresomin_black].to_excel(writer, sheet_name="ClientesBlack", index=False, engine="xlsxwriter")

#Grabamos el archivo
writer.save()
writer.close()

