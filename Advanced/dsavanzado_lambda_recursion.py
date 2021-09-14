x=5
y=7


sumar_numeros = lambda x,y : x + y


#usando variables
print("resultado= ",sumar_numeros(x,y)) 

#usando numeros enteros
print("resultado= ",sumar_numeros(10,7)) 


print("resultado= ",sumar_numeros(
    sumar_numeros(1,1),7
    )
    ) 
