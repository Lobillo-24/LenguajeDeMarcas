import random

palabras = ["python", "ahorcado", "programacion", "codigo", "juego"]
palabra = random.choice(palabras).upper()

lista1 = list(palabra)
lista2 = ["-"] * len(lista1)

ahorcado = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

dificultad = input("Elige dificultad (facil, medio, dificil): ").lower()
if dificultad == "facil":
    intentos = 10
elif dificultad == "medio":
    intentos = 7
else:
    intentos = 5

intentos_iniciales = intentos
letras_usadas = []

while intentos > 0:
    indice = 6 - int((intentos * 6) / intentos_iniciales)
    if indice > 6:
        indice = 6
    
    print(ahorcado[indice])
    print("Palabra: " + " ".join(lista2))
    print("Letras usadas:", " ".join(letras_usadas))
    
    letra = input("Escribe una letra: ").upper()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Debes escribir solo una letra.")
        continue
    
    if letra in letras_usadas:
        print("Ya usaste esa letra.")
        continue
    
    letras_usadas.append(letra)
    
    if letra in lista1:
        for i in range(len(lista1)):
            if lista1[i] == letra:
                lista2[i] = letra
        print("¡Bien!")
    else:
        intentos -= 1
        print("Fallaste. Intentos restantes:", intentos)
    
    if "-" not in lista2:
        print("¡Ganaste! 🎉")
        print("La palabra era:", palabra)
        break

if "-" in lista2:
    print(ahorcado[6])
    print("Perdiste 😢")
    print("La palabra era:", palabra)