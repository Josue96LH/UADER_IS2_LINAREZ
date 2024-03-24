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


if len(sys.argv) < 2:
    while True:
        try:
            rango = input("Ingrese un rango de números en el formato desde-hasta (ej. 4-8): ")
            desde, hasta = map(int, rango.split('-'))
            if desde > hasta:
                print("El primer número debe ser menor o igual que el segundo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un rango válido en el formato desde-hasta.")
else:
    rango = sys.argv[1]
    desde, hasta = map(int, rango.split('-'))
    if desde > hasta:
        print("El primer número debe ser menor o igual que el segundo.")
        sys.exit()

calcular_factoriales(desde, hasta)
