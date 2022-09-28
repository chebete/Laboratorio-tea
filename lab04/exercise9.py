maximo = 0
minimo = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while True:
 try:
    numero = input("Por favor ingrese un numero\n>>> ")
    if (numero == "done"):
        break
    else:
     if int(maximo) < int(numero):
        maximo = numero
     if int(minimo) > int(numero):
        minimo = numero
 except:
       print("ingrese valores validos")
       continue
print("maximo: "+ str(maximo))
print("minimo: "+ str(minimo))