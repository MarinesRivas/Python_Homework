

class person:
    def init(self, name, age, x):
        self.name = name
        self.age = age
        self.x = x
    def myName(self):
        print("Hi my name is Victor" + self.name)
    
    def myAge(self):
        print("My age is" + self.age)
    
    def escribir(self):
        print("Dame x" + self.age)


print(":::::::::::")

print("Herencia")

class Animal:
    def _init_(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self)._name_)


# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")

print(":::::::::")

print("Cohesion")

# Mal. Cohesión débil
def suma():
    num1 = float(input("Dame primer número"))
    num2 = float(input("Dame segundo número"))
    suma = num1 + num2
    print(suma)

suma()
def suma(numeros):
    total = 0
    for i in numeros:
        total = total + i
    return total

print("::::::::::::::::::::::")

print("Abstraccion")

class Clase:
    def _init_(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo
    mi_clase = ("valor_atributo")
#mi_clase.mi_atributo
# 'valor_atributo'

print("::::::::::::")

print("Poliformismo")
class Animal:
    def hablar(self):
        pass
class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
for animal in Perro(), Gato():
    animal.hablar()

print(":::::::::")

print("Acoplamiento")

class Clase1:
    x = True
    pass

class Clase2:
    def mi_metodo(self, valor):
        if Clase1.x:
            self.valor = valor

mi_clase = Clase2()
mi_clase.mi_metodo("Hola")
mi_clase.valor

print(":::::::::")

print("Encapsulamiento")

class Clase:
    atributo_clase = "Hola"
    def _init_(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

mi_clase = Clase("Que tal")
mi_clase.atributo_clase
mi_clase.atributo_instancia
# 'Hola'
# 'Que tal'

class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok