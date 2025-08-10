class Employee:
    __minsalary = 5000
    maxsalary = 50000
    _companyname = "ABC Corp."

    def __init__(self, name, salary, department):       # Constructor
        self.__name = name
        self.__salary = salary
        self.departmet = department
        

    def display(self):
        print("Employee Name = " + self.__name)             # String ' + or ,format() '
        print("Salary = ",format(self.__salary))            # Numeric ' ,format() '
        print("Department Name = ",format(self.departmet))


class Accounting(Employee):
    department = "Accounting"

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.department)
        self.__age = age

    def display(self):
        super().display()
        print("Age =",format(self.__age))

class Programmer(Employee):
    department = "Programmer"

    def __init__(self, name, salary):
        super().__init__(name, salary, self.department)

    def display(self):
        super().display()
    

class Sale(Employee):
    department = "Sale"

    def __init__(self, name, salary):
        super().__init__(name, salary, self.department)

    def display(self):
        super().display()
    


Em1 = Accounting("Kong", 10000, 45)
Em2 = Programmer("Jojo", 40000)
Em3 = Sale("Nutty", 35000)

print("------------------Em1--------------------")
Em1.display()
print("------------------Em2--------------------")
# Em2.display()
print("------------------Em3--------------------")
Em3.display()

print("######################################")
# print(Employee.__minsalary)           # Error because it's private variable
print(Employee.maxsalary)
print(Employee._companyname)