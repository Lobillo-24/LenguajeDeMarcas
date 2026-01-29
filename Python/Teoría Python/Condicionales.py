#Condicionales 1

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Hola")

#Condicionales 2

nota = float(input("Introduce la nota: "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

#Condicionales 3

nota2 = float(input("Introduce tu nota: \n"))

match nota2:
    case 0|1|2|3|4:
        print("Suspenso")
    case 5|6|7:
        print("Aprobado")
    case 8|9:
        print("Notable")
    case 10:
        print("Sobresaliente")