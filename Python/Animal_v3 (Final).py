class animal:
    name = None
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"This animal named {self.name} sound ...")

class dog(animal):
    def sound(self):
        print(f"The dog {self.name} sound Woof")

class cat(animal):
    def sound(self):
        print(f"The cat {self.name} sound Meow")



k = animal("Juan")
k1 = dog("Bob")
k2 = cat("Max")

k.sound()
k1.sound()
k2.sound()