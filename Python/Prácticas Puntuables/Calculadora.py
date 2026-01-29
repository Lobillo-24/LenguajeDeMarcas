repetir = True

while repetir:
    print("MENU")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")

    escoger = int(input("Escoge una opción: "))

    if escoger == 5:
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        repetir = False

    elif escoger == 1 or escoger == 2 or escoger == 3 or escoger == 4:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if escoger == 1:
            print("Resultado:", num1 + num2)

        elif escoger == 2:
            print("Resultado:", num1 - num2)

        elif escoger == 3:
            print("Resultado:", num1 * num2)

        elif escoger == 4:
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("No se puede dividir entre cero")

    else:
        print("Opción no válida. Debes elegir un número del 1 al 5.")