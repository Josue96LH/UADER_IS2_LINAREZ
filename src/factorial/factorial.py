#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys


# Función para calcular el factorial de un número
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


# Función para calcular y mostrar los factoriales en un rango dado
def calcular_factoriales(desde, hasta):
    for num in range(desde, hasta + 1):
        print("El factorial de", num, "es", factorial(num))


# Función para procesar el rango ingresado por el usuario
def procesar_rango(rango):
    partes = rango.split('-')  # Dividir la cadena en partes usando el guión como separador
    if len(partes) == 1:  # Si solo se proporciona un número
        numero = int(partes[0])
        if numero < 1:  # Verificar si el número es válido
            print("El número debe ser mayor o igual que 1.")
            sys.exit()
        calcular_factoriales(1, numero)  # Calcular factoriales desde 1 hasta el número dado
    elif len(partes) == 2:  # Si se proporciona un rango
        if partes[0]:  # Si hay un límite inferior
            desde = int(partes[0])
        else:
            desde = 1  # Si no se proporciona, establecer límite inferior en 1
        if partes[1]:  # Si hay un límite superior
            hasta = int(partes[1])
        else:
            hasta = 60  # Si no se proporciona, establecer límite superior en 60
        if desde > hasta:  # Verificar si el rango es válido
            print("El primer número debe ser menor o igual que el segundo.")
            sys.exit()
        calcular_factoriales(desde, hasta)  # Calcular factoriales dentro del rango
    else:
        print("Formato de rango incorrecto.")  # Mensaje de error si el formato del rango es incorrecto
        sys.exit()


# Comprobar si se proporciona un rango desde la línea de comandos o solicitarlo al usuario
if len(sys.argv) < 2:
    while True:
        rango = input("Ingrese un rango de números en el formato desde-hasta (ej. 4-8), o indique solo el límite superior (-10): ")
        procesar_rango(rango)  # Procesar el rango ingresado
else:
    rango = sys.argv[1]
    procesar_rango(rango)  # Procesar el rango proporcionado desde la línea de comandos
