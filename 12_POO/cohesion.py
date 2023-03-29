
# Mal. Cohesión débil#
def suma():
    num1 = float(input("Dame primer número"))
    num2 = float(input("Dame segundo número"))
    suma = num1 + num2
    print(suma)
suma()


# Bien. Cohesión fuerte#
def suma(numeros):
    total = 0
    for i in numeros:
        total = total + i
    return total
