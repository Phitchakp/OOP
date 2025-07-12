'''
## Ver1 : Create class and subclass for each Animmal

class Animal:
    def __init__(self):
        pass


class Rabbit(Animal):
    def __init__(self, name, age, runspeed):
        self.name = name
        self.age = age
        self.runspeed = runspeed


class Fish(Animal):
    def __init__(self, name, age, swinspeed):
        self.name = name
        self.age = age
        self.swinspeed = swinspeed


class Hawk(Animal):
    def __init__(self, name, age, flyspeed):
        self.name = name
        self.age = age
        self.flyspeed = flyspeed

k1 = Rabbit("BugsBunny", 1, 25)

-----------------------------------------------------------------------------'''
'''
## Ver 2 : Remove name & age in each animal then replace 'super().__init__(v1,v2)' and name & age in Class
##         Because they have the same property

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Rabbit(Animal):
    def __init__(self, name, age, runspeed):
        super().__init__(name, age)
        self.runspeed = runspeed


class Fish(Animal):
    def __init__(self, name, age, swinspeed):
        super().__init__(name, age)
        self.swinspeed = swinspeed


class Hawk(Animal):
    def __init__(self, name, age, flyspeed):
        super().__init__(name, age)
        self.flyspeed = flyspeed

k1 = Rabbit("BugsBunny", 1, 25)
k2 = Fish("Nemo", 3, 12)

print(k1.name)
print(k2.name)
print(k2.age)
print(k2.swinspeed)
print(f"The {k2.name} swims at a speed of {k2.swinspeed} mph")          # f ==  formatted string literal (f-string)
print("The " + k2.name + " swims at a speed of " + str(k2.swinspeed) + " mph")

-----------------------------------------------------------------------------'''
'''
## Ver 3 : Define "Run" in Rabbit, "Swim" "Fly"

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Rabbit(Animal):
    def __init__(self, name, age, runspeed):
        super().__init__(name, age)
        self.runspeed = runspeed

    def run(self):
        print(f"This {self.name} can run")



class Fish(Animal):
    def __init__(self, name, age, swinspeed):
        super().__init__(name, age)
        self.swinspeed = swinspeed

    def swim(self):
        print(f"This {self.name} can swim")


class Hawk(Animal):
    def __init__(self, name, age, flyspeed):
        super().__init__(name, age)
        self.flyspeed = flyspeed

    def fly(self):
        print(f"This {self.name} can fly")


k1 = Rabbit("BugsBunny", 1, 25)
k2 = Fish("Nemo", 3, 12)

k1.run()
k2.swim()

-----------------------------------------------------------------------------'''

## Ver 4 : Define "move" in Animal Class & 'super().move(v3)' for each animals

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self, speed):
        print(f"The {self.name} moves at a speed of {speed} mph")


class Rabbit(Animal):
    def __init__(self, name, age, runspeed):
        super().__init__(name, age)
        self.runspeed = runspeed

    def run(self):
        print(f"This {self.name} can run")
        super().move(self.runspeed)


class Fish(Animal):
    def __init__(self, name, age, swinspeed):
        super().__init__(name, age)
        self.swinspeed = swinspeed

    def swim(self):
        print(f"This {self.name} can swim")
        super().move(self.swinspeed)


class Hawk(Animal):
    def __init__(self, name, age, flyspeed):
        super().__init__(name, age)
        self.flyspeed = flyspeed

    def fly(self):
        print(f"This {self.name} can fly")
        super().move(self.flyspeed)


k1 = Rabbit("BugsBunny", 1, 25)
k2 = Fish("Nemo", 3, 12)

k1.run()
k2.swim()    