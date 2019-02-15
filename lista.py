#!/usr/bin/env/ python

lista = [1,2,'3', ('uno','dos',3)]

print(type(lista))

print (lista)

print(lista[0])

print(lista[3][-2])

lista.append('nuevo')

print(lista)
#verifica los valores
for item in lista:
    print(item)
    #Separa los item
    if type(item)==tuple:
        #separa las tuple
        for itemnew in item:
            #Imprimir las tuple
            print(itemnew) 