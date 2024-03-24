#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys


def factorial(num):
    if num < 0:
        print("El factorial de un número negativo no existe")
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact


def calcular_factoriales(desde, hasta):
    for num in range(desde, hasta + 1):
        print("El factorial de", num, "es", factorial(num))


def procesar_rango(rango):
    partes = rango.split('-')
    if len(partes) == 1:
        numero = int(partes[0])
        if numero < 1:
            print("El número debe ser mayor o igual que 1.")
            sys.exit()
        calcular_factoriales(1, numero)
    elif len(partes) == 2:
        if partes[0]:  # Si hay un límite inferior
            desde = int(partes[0])
        else:
            desde = 1
        if partes[1]:  # Si hay un límite superior
            hasta = int(partes[1])
        else:
            hasta = 60
        if desde > hasta:
            print("El primer número debe ser menor o igual que el segundo.")
            sys.exit()
        calcular_factoriales(desde, hasta)
    else:
        print("Formato de rango incorrecto.")
        sys.exit()


if len(sys.argv) < 2:
    while True:
        rango = input("Ingrese un rango de números en el formato desde-hasta (ej. 4-8), o indique solo el límite superior (-10): ")
        procesar_rango(rango)
else:
    rango = sys.argv[1]
    procesar_rango(rango)
