class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self, speed):
        print(f"The {self.name} moves at a speed of {speed}mph")


class Rabbit(Animal):
    def __init__(self, name, age, run_speed):
        super().__init__(name, age)
        self.run_speed = run_speed

    def run(self):
        print(f"This {self.name} can run")
        super().move(self.run_speed)


class Fish(Animal):
    def __init__(self, name, age, swim_speed):
        super().__init__(name, age)
        self.swim_speed = swim_speed

    def swim(self):
        print(f"This {self.name} can swim")
        super().move(self.swim_speed)


class Hawk(Animal):
    def __init__(self, name, age, fly_speed):
        super().__init__(name, age)
        self.fly_speed = fly_speed

    def fly(self):
        print(f"This {self.name} can fly")
        super().move(self.fly_speed)


# Create instances
rabbit = Rabbit("rabbit", 1, 25)
fish = Fish("fish", 2, 12)
hawk = Hawk("hawk", 3, 50)

# Call their specific methods
rabbit.run()
fish.swim()
hawk.fly()