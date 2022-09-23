print("Bienvenido!")
def calculopago(horas, pago):
    if float(horas) > 40:
        extra = float(horas) - 40
        salario = 40*float(pago) + 1.5*float(pago)*float(extra)
        print("Usted recibira "+ str(salario)+ " Lempiras")
    else:
        salario = float(horas)*float(pago)
        print("Usted recibira "+ str(salario)+ " Lempiras")
    return salario

try:
 horas = input("Ingrese el numero de Horas trabajadas\n")
 pago = input("Ingrese el pago por Hora\n")
 calculopago(horas, pago)
except:
    print("ingrese valores numericos")