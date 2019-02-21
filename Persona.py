#!/usr/bin/env python

class Persona:

    altura = 1.80

    def __init__(self,altura=1.77,Nombre="Jose Esparza"):
        self.altura = altura
        self.Nombre = "Ramon"

    def saludo(self, mensaje):
        print(mensaje)

Ramon_ =Persona(1.75,"Ramon")

Ramon_.saludo("Hola, Buenos dias")

print(Ramon_.Nombre)

Ramon_.Nombre = "Jose"

print(Ramon_.Nombre)

Ramon_.Apellido = "Agramon"

print(Ramon_.Apellido)

Cesar = Persona()

#print (Cesar.Apellido)