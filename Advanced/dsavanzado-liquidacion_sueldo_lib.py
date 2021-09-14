#Creamos las variables de los descuentos
descuento_jubilacion = 0.11
descuento_obrasocial = 0.20
descuento_cuotasindical = 0.03
descuento_ganancias = 0.35

def calculo_sueldoneto(sueldo_bruto):
    sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_jubilacion)
    sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_obrasocial)
    sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_cuotasindical)
    
    if (sueldo_bruto>=100000):
        sueldo_neto=sueldo_bruto-(sueldo_bruto*descuento_jubilacion)
        
    return sueldo_neto

