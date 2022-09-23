

def calcula_calificacion(notes):
 if notes >= 0 and notes <= 10:
    if notes > 9:
        grade = print("sobresaliente")
    elif notes >8 and notes <=9:
        grade = print("notable")
    elif notes >7 and notes <=8:
        grade = print("Bien")
    elif notes >6 and notes <=7:
        grade = print("Suficiente")
    elif notes <=6:
        grade = print("Insuficiente")
    elif notes == 10:
        grade = print("sobresaliente")
    return grade

print("BIENVENIDO!")
try:
 notes = float(input("Ingrese la calificacion\n"))
 calcula_calificacion(notes)
except:
    print("Ingrese un valor dentro del rango 0-10 o un valor numerico.")