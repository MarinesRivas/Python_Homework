# Variables en Python

first_name = 'Marines'
last_name = 'Rivas'
country = 'Mexico'
city = 'Zacatecas'
age = 29
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Marines', 
    'lastname':'Rivas', 
    'country':'Mexico',
    'city':'Zacatecas'
    }

# Imprimir los valores almacenados en las variables

print('Nombre:', first_name)
print('Longitud del nombre:', len(first_name))
print('Apellido: ', last_name)
print('Longitud del apellido: ', len(last_name))
print('Pais: ', country)
print('Ciudad: ', city)
print('Edad: ', age)
print('Habilidades: ', skills)
print('Información personal: ', person_info)

# Declarar múltiples variables en una línea

first_name, last_name, country, age = 'Marines', 'Rivas', 'Mexico', 29

print(first_name, last_name, country, age)
print('Nombre:', first_name)
print('Morgan: ', last_name)
print('México: ', country)
print('Edad: ', age)