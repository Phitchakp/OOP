from Employee_Class import Employee

class Sale(Employee):
    department = "Sale"

    def __init__(self, name, salary, area, bonus, overtime):
        super().__init__(name, salary, self.department, bonus, overtime)
        self.area = area

    def display(self):
        super().display()
        print("Area, Zone =" + self.area)
    
    def __str__(self):
        return print(super().__str__() ,", Area = {}" .format(self.area))