# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:40:36 2024

@author: Katherine
"""
# Pregunta 01
nombre = input("Ingrese nombre de usuario: ")
print("¡Hola, "+nombre + "!")

# Pegunta 02
# Solicitamos el costo de su comida
costo = int(input("¿Cuanto fue el costo de su consumo?: "))
# Solicitamos el porcentaje de propina que desear agregar a la cuenta
porcentaje = int(input("¿Que porcentaje desea agregar de propina?: "))
# Realizar el cálculo con una estructura selectiva (>= 15%)
if porcentaje >= 15:
    propina = costo*(porcentaje/100)
    print("Debe agregar "+str(propina)+" $ de propina")
else:
    print("El porcentaje de propina de ser mayor o igual al 15%")

# Pregunta 03
# Solicitar al usuario el número de payasos y muñecas
payasos = int(input("Ingrese el número de payasos vendidos:"))
muñecas = int(input("Ingrese el número de muñecas vendidas:"))
# Mostremos resultado del peso que sera enviado a logística
peso_total = (payasos*112)+(muñecas*75)
print("El peso total del paquete es "+str(peso_total)+" g.")

# Pregunta 04
numero = int(input("Ingrese un número entero: "))
suma = numero*(numero+1)/2
print("La suma de los primeros "+str(numero)+" es igual a "+str(suma))

# Pregunta 05
n_shows = int(input("¿Cuantos shows musicales ha visto el ultimo año?: "))
if n_shows >= 3:
    print("el usuario ha visto 3 o más shows músicales: "+str(n_shows >= 3))
else:
    print("el usuario ha visto 3 o más shows músicales: "+str(n_shows >= 3))

# Pregunta 06
edad = int(input("¿Qué edad tiene?: "))
if edad <= 4 and edad > 0:
    print("Precio de entrada: GRATIS ")
elif edad > 4 and edad <= 18:
    print("Precio de entrada: 5 $ ")
elif edad > 18:
    print("Precio de entrada: 10$ ")
else:
    print("dato no valido")

# Pregunta 07

n_1 = int(input("Ingrese el primer número: "))
n_2 = int(input("Ingrese el segundo número: "))

print("Menú de opciones")
print("================")
print("(1) = suma ")
print("(2) = resta ")
print("(3) = multiplicación ")

opcion = int(input("Ingrese una opción de cálculo:"))
if opcion == 1:
    suma = n_1+n_2
    print("El resultdo es: "+str(suma))
elif opcion == 2:
    resta = n_1-n_2
    print("El resultdo es: "+str(resta))
elif opcion == 3:
    multi = n_1*n_2
    print("El resultdo es: "+str(multi))
else:
    print("La opción no es valida")

# Pregunta 08

hora = input("Ingrese la hora: ")
hora_lista = hora.split(":")
hora_conver = float(".".join(hora_lista))
print(hora_conver)

if hora_conver >= 7.0 and hora_conver <= 8.0:
    print("Es hora de desayunar")
elif hora_conver >= 12.0 and hora_conver <= 13.0:
    print("Es hora de almorzar")
elif hora_conver >= 18.0 and hora_conver <= 19.0:
    print("Es hora de cenar")

# Pregunta 09
texto = input("Escriba: Di buen día a papá: ")
lista1 = texto.split()
print(lista1)
lista1.reverse()
print(lista1)

# Pregunta 10

elementos2 = input("Escriba 6 elementos con separación en blanco: ")
lista2 = elementos2.split()
print(lista2)
del lista2[0]
print(lista2)
del lista2[3]
print(lista2)
del lista2[3]
print(lista2)

# Pregunta 11

elementos3 = input("Escriba n números: ")
lista3 = elementos3.split()
print(lista3)
lista3_unico = list(set(lista3))
print(lista3_unico)
