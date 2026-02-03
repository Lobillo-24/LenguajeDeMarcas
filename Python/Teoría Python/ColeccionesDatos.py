#LISTAS

numeros = [1,2,3,4,5]
nombres = ["Ana","Luis","Carlos"]
mezcla = [1,"Hola",True,3.14]

print(numeros)
print(nombres[1])
print(type(numeros))

for nom in nombres:
    print(nom)

#DICCIONARIOS

persona = {
    "nombre":"Ana",
    "edad":20,
    "ciudad":"Madrid"
}

print(persona["nombre"])
print(type(persona))

for per in persona:
    print(per)

#SETS
colores = set(["rojo","verde","azul","rojo"])
print(colores)
colores.add("amarillo")
print(colores)

#TUPLAS
colores = ("rojo","verde","azul")
print(colores[0]) # rojo
print(colores[2]) # azul

#Ahorcado
lista1 = ["C","A","S","A"]
lista2 = ["-","-","-","-"]

#for list in lista2:
    #if list !='-' #El jugador ha ganado