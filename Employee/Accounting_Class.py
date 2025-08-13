from Employee_Class import Employee

class Accounting(Employee):                                     # Inheritance       # Subclass
    department = "Accounting"

    def __init__(self, name, salary, age, bonus, overtime):                      # Polymorphism 1
        super().__init__(name, salary, self.department, bonus, overtime)         # Super
        self.__age = age

    def display(self):                                          # Polymorphism 2
        super().display()
        print("Age =", format(self.__age))

    def __str__(self):
        return print(super().__str__() ,", Age = {}" .format(self.__age))