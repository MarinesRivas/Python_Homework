
#MARIA INES RIVAS RECEDNEZ#

"""
CICLOS
"""

numeros = [0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]
i=0
for i in range(i,len(numeros)): # el número es un nombre temporal para referirse a los elementos de la lista, válido solo dentro de este ciclo
    print(i)       # los números se imprimirán línea por línea, del 0 al 5

print(i+1) # numeros en linea mas el siguiente termino en este caso el 16

for i in range (i,len(numero), 2):

    print(i)

#diccionario#

    persona = {
    'nombre':'Marines',
    'apellido':'Rivas',
    'edad':29,
    'pais':'México',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'

    }}

    print('###################')
    for llave in persona:
        if llave=='skills':
            for skill in persona['skills']:
                print(skill)

break
else:

print("no esta")






