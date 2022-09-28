contador = 0
suma = 0 
while True:
    try:
        print("Ingrese un numero\nSi desea finalizar ingrese <done>")
        numer = input(">>>")
        if (numer == "done"):
            break
        else:
            contador = float(contador) +1
            suma = float(suma) + float(numer)
            media = float(suma) / float(contador)
    except:
            print("Dato no Valido")
            #reduje en 1 porque, porque tomaba encuenta en el contador los ingresos no validos.
            contador = float(contador) -1
            continue
print("Numero de entradas: "+ str(contador))
print("Acumulado: "+ str(suma))
print("Media: "+ str(media))