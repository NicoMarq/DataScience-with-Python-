#Defino la Funcion para Ingreso a Boliche

def chequear_adulto(edad):
    if edad>=18:
        return  "OK BIENVENIDO"
    else:
        return "SOS MENOR, A CASA"
    
#Defino la variable
mi_edad = int(input("Ingresá tu edad: "))

print(chequear_adulto(mi_edad))