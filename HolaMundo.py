#!/usr/bin/env python

texto1, texto2 = "Hola Mundo", "que rollo"

texto12 = 12

print(texto12)

textoMultilinia = """Esto es un texto
multilinia
y puedo manejar un texto largo, en parrafos
sin necesidad de usar saltos de linia"""

print(textoMultilinia)

nombre = "Ramón"
apellido = "Agramón"
edad = 22

print("Hola: {1} {0} y tienes {2}".format(nombre, apellido, edad))

nombreCompleto = f"Hola: {nombre} {apellido} tienes {edad} años"

contador = 0

while(contador <= 3):
    print(contador)
    contador+=1

for numero in range(3):
    print(numero+1)
    if numero == 2:
        print("fin del ciclo")
    else:
        print("todavia no")



print(nombreCompleto)
