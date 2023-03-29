


class Person:
    def _init_(self,name,age,x):
        self.name = name
        self.age = age
        self.x = x

    def myName(self):
        print("hello my name is " + self.name)

    def myAge(self):
        print("hello my age is" + self.age)

    def escribir(self):
        print(self.x)

p1 = Person("John", 36, 10)

del p1.name

print(p1.name)

print()
