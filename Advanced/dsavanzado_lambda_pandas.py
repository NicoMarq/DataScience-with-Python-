import pandas as pd

mis_empleados=pd.DataFrame(
    {
    'nombre':['Pedro','Jorge','Jessica','Deborah','Julio'],
    'edad':[20,25,15,10,30],
    'sueldo':[2000,3500,1950,1950,10000]
    }
)



mis_empleados['sueldo 2021']=mis_empleados.apply(
    lambda x:
        x['sueldo']*1.2,axis=1
    )
    
    
print (mis_empleados)
