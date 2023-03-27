

#MARIA INES RIVAS RECENDEZ#

"""
Funciones

"""


def generar_nombre_completo ():
    nombre = 'Marines'
    apellido = 'Rivas'
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    return nombre_completo
print(generar_nombre_completo())

def agregar_dos_numeros ():
    numero_uno = 10
    numero_dos = 30
    total = numero_uno + numero_dos
    return total
print(agregar_dos_numeros())

print("############################################")

def saludo (nombre):
    mensaje = nombre + ', Bienvenido al taller de python!'
    return mensaje

print(saludo('Marines'))

def agrega_diez(numero):
    diez = 10
    return numero + diez
print(agrega_diez(90))

def numero_al_cuadrado(x):
    return x * x
print(numero_al_cuadrado(2))

def area_del_circulo (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_del_circulo(10))

def suma_de_numeros(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(suma_de_numeros(10)) # 55
print(suma_de_numeros(100)) # 5050

print("############################################")

def generar_nombre_completo (nombre, apellido):
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    return nombre_completo
print('Nombre completo: ', generar_nombre_completo('Marines','Rivas'))

def suma_dos_numeros (numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    return suma
print('Suma de dos numeros: ', suma_dos_numeros(1, 9))

def calcular_edad (año_actual, año_nacimiento):
    edad = año_actual - año_nacimiento
    return edad

print('Edad: ', calcular_edad(2023, 1993))

def peso_de_objeto (masa, gavedad):
    peso = str(masa * gavedad)+ ' N' # el valor tiene que ser cambiado a una cadena primero
    return peso
print('Peso de un objeto en Newtons: ', peso_de_objeto(100, 9.81))

print("############################################")

def saludo (nombre = 'Marines'):
    mensaje = nombre + ', bienvenido a python!'
    return mensaje
print(saludo())
print(saludo('Alberto'))

def generar_nombre_completo (nombre = 'Marines', apellido = 'Rivas'):
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    return nombre_completo

print(generar_nombre_completo())
print(generar_nombre_completo('MariaInes','Rivas-Recendez'))

def calcular_edad (año_nacimiento,año_actual = 2023):
    edad = año_actual - año_nacimiento
    return edad
print('edad: ', calcular_edad(1993))

def peso_de_objeto (masa, gavedad = 9.81):
    peso = str(masa * gavedad)+ ' N' # el valor tiene que ser cambiado a cadena primero
    return peso
print('peso de un objeto en newtons: ', peso_de_objeto(100)) # 9.81 - promedio de gavedad en la superficie de la Tierra
print('peso de un objeto en newtons: ', peso_de_objeto(100, 1.63)) # gravedad en la superficie de la Luna




