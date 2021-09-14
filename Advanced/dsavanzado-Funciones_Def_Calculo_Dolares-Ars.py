#DEFINO LA VARIABLE CON EL TIPO DE CAMBIA
exchange_rate_ARS = 150

#DEFINO LA FUNCION CON EL PARAMETRO PESOS
def conversion(pesos):
    dolares = pesos/exchange_rate_ARS
    
    return dolares

#LE PIDO AL USUARIO QUE INGRESE LA CANTIDAD DE PESOS 
#QUE SERÁ EL PARAMETRO DE LA FUNCION
pesos = float(input("INGRESE CANTIDAD DE PESOS: "))

#IMPRIMO LLAMANDO A LA FUNCION
print ("LE CORRESPONDE:", conversion(pesos), "DOLARES")
    
