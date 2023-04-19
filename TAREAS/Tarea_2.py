
#MARIA INES RIVAS RECENDEZ

#TAREA 2

"""
Expresiones y Operadores
"""

#OPERADORES


# Operador +.
a = 7 + 3
print(a)
a = 5
b = 3
c = a + b
print(c)
print(3+4)  #+  Este es el operador de suma y realiza la función de adicionar un operando al otro.

#Operador -.
a = 6 - 2
print(a)
a = 5
b = 3
c = a - b
print(c)
print(2-6)   #- Este es el operador de resta y realiza la función de sustraer un operando de otro.

#Operador *.
a = 3 * 4
print(a)
a = 6
b = 3
c = a * b
print(c)
print(5*7)   #* Este es el operador de multiplicación y realiza la función de aumentar un operando en función de otro operando.

#Operador /.
a = 6 / 2
print(a)
a = 5
b = 3
c = a / b
print(c)
print(10/3)   #/ Este es el operador de división y realiza la función de seccionar un operando en función de otro operando.

#Operador %.
a = 8 % 4
print(a)
a = 9
b = 2
c = a % b
print(c)
print(6%3)   #%  Este es el operador de módulo y realiza la función de regresar el residuo de una división.

#Operador **.
a = 3 ** 3
print(a)
a = 2
b = 4
c = a ** b
print(c)
print(4**3)    #** - Este es el operador de exponencial y permite obtener la potencia de un operando en función de otro operando.


#EXPRESIONES RELACIONALES


#Operador <.
# < - Este es el operador de menor que, y se utiliza en las expresiones relacionales para saber si un operando es menor a otro operando.
a = 3 < 3
print(a)
a = 2
b = 4
c = a < b
print(c)
print(4<3)

#Operador >.
# > - Este es el operador de mayor que, y se utiliza en las expresiones relacionales para saber si un operando es mayor a otro operando.
a = 4 > 2
print(a)
a = 5
b = 7
c = a > b
print(c)
print(9>2)

#Operador ==.
# == - Este es el operador de igual que, y se utiliza en las expresiones relacionales para saber si un operando es igual a otro operando.
a = 5 == 5
print(a)
a = 6
b = 9
c = a == b
print(c)
print(6==2)

#Operador !=.
# != - Este es el operador desigual que, y se utiliza en las expresiones relacionales para saber si un operando es diferente a otro operando.
a = 4 != 2
print(a)
a = 5
b = 3
c = a != b
print(c)
print(8!=8)

#Operador <=.
# <= - Este es el operador de menor igual que, y se utiliza en las expresiones relacionales para saber si un operando es menor o igual a otro operando.
a = 5 <= 3
print(a)
x = 7
y = 5
z = x <= y
print(z)
print(9<=4)

#Operador >=.
# >= Este es el operador de mayor igual que, y se utiliza en las expresiones relacionales para saber si un operando es mayor igual a otro operando.
a = 2 >= 8
print(a)
a = 3
b = 4
c = a >= b
print(c)
print(7>=3)



#EXPRESIONES LOGICAS.




#Operador and.
# and - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
print(4-1==3 and 5>6)
print(6+7 > 11 and 3==3)

#Operador or.
# or - Este es el operador lógico para realizar una conjugación, si cualquiera de los operandos presentes no se cumple en la expresión lógica, esta resulta en False, caso contrario, si toda la expresión lógica de conjugación se cumple el resultado es True.
print(4-1==3 or 5>6)
print(6+7 > 11 or 3==3)

#Operador not.
#not - Este es el operador lógico para realizar una negación, si el operando no se encuentra en el otro operando, la expresión se cumple y resulta en True, caso contrario, si la expresión no se cumple el resultado es False.
print(not 5>6)
print(not 5>4)



#EXPRESIONES DE CARACTER



import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
re.findall(patron, frase)

