
class A:
    def __init__(self,a1):
        self.a1 = a1

    def sound(self):
        print("This animal sound", self.a1)

class B(A):
    def sound(self):
        print("The dog sound", self.a1)

class C(A):
    def sound(self):
        print("The cat sound", self.a1)



k = A("!!!")
k1 = B("Woof")
k2 = C("Meow")

k.sound()
k1.sound()
k2.sound()



# ------------------------------------------------------------------------------------------------

class animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("This animal sound", self.name)

class dog(animal):
    def sound(self):
        print("The dog sound", self.name)

class cat(animal):
    def sound(self):
        print("The cat sound", self.name)



k = animal("!!!")
k1 = dog("Woof")
k2 = cat("Meow")

k.sound()
k1.sound()
k2.sound()
