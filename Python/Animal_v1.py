class animal:
    def __init__(self,a1):
        self.a1 = a1

    def sound(self):
        print("This animal sound", self.a1)

class dog(animal):
    def sound(self):
        print("The dog sound", self.a1)

class cat(animal):
    def sound(self):
        print("The cat sound", self.a1)



k = animal("!!!")
k1 = dog("Woof")
k2 = cat("Meow")

k.sound()
k1.sound()
k2.sound()
