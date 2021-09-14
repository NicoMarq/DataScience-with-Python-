import pandas as pd
from sqlalchemy import create_engine


conexion = create_engine('mysql+mysqlconnector://root:mipass@127.0.0.1:3306/nombrebase?charset=utf8', echo=False)



categorias_df=pd.read_excel("C:/Users/Nico/Desktop/Ejemplo.xls")


print (categorias_df)


categorias_df.to_sql(name='nombre_tabla', 
                       con=conexion, 
                       if_exists = 'replace', 
                       index=False)

    