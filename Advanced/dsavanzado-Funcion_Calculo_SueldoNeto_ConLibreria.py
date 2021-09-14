import liquidacion_sueldo_lib as liqargy

sueldo_bruto = float(input("Ingrese su sueldo Bruto: "))

sueldo_neto = liqargy.calculo_sueldoneto(sueldo_bruto)

print("Le corresponde el siguiente Sueldo Neto: ", sueldo_neto)