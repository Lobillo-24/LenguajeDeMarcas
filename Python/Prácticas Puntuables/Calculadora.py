repetir = True

while repetir:

    print("\nMENU")
    print("----------")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")

    try:
        escoger = int(input("Escoge una opción: "))
    except ValueError:
        print("Introduce una opción válida (número del 1 al 5)")
        continue

    if escoger == 5:
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        repetir = False

    elif escoger >= 1 and escoger <= 4:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Debes introducir números válidos")
            continue

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
        print("Opción no válida. Elige una opción del menú.")