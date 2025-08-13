from Employee_Class import Employee

class Programmer(Employee):
    department = "Programmer"

    def __init__(self, name, salary, experience, skill, bonus, overtime):
        super().__init__(name, salary, self.department, bonus, overtime)
        self.__experience = experience
        self.__skill = skill

    def display(self):
        super().display()
        print("Working Experience = ", format(self.__experience))
        print("Skill = " + self.__skill)

    def __str__(self):
        return print(super().__str__() ,", Exp = {} years, Skill = {}" .format(self.__experience, self.__skill))
