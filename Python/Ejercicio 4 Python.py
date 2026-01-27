import math

cateto1 = float(input("Ingresa el primer cateto: "))
cateto2 = float(input("Ingresa el segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"La hipotenusa es: {hipotenusa}")