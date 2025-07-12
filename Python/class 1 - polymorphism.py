class Animal:
    name: str
    def __init__(self, name:str):
        self.name = name
        
    def make_sound(self):
        # do nothing
        return

class Dog(Animal):
    __breed:str
    __is_hungry:bool
    def __init__(self, name:str, breed:str):
        Animal.__init__(self, name)
        self.__breed = breed
        self.__is_hungry = True
    
    def make_sound(self):
        print(f'Woof! {self.name} is barking')
        
    def check_is_hungry(self):
        return self.__is_hungry

    def feed(self):
        if self.__is_hungry == True:
            print("Eating")
        else:
            print("The dog is not eating")
        if self.__breed == 'Pitbul':
            self.__is_hungry = True
        else:
            self.__is_hungry = False
        state = "hungry" if self.__is_hungry else "not hungry"
        print(f"The dog eat and is {state}")
        



bob:Dog = Dog("Bob", "Pitbul")
bob.feed()
bob.feed()

john:Dog = Dog("John", "Golden")
john.feed()
john.feed()

class Cat(Animal):
    def __init__(self, name:str):
        Animal.__init__(self, name)
    
    def make_sound(self):
        print(f'Meow! {self.name} is meowing')

titi:Cat = Cat("Titi")

my_list:list = [bob, titi]

for animal in my_list:
    animal.make_sound()