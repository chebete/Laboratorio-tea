maximo = 0
#Trate de hacerlo lo mas simple posible por ello di un numero grande comparativo para minimo, para que pueda
#ser True la condicion para minimo y luego se vaya actualizando con los inputs. 
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