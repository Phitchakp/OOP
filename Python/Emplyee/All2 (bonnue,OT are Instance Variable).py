class Employee:                                                 # Encapsulation     # Class
    __minsalary = 5000                                          # Attribute, Proporty   # Class variable (no need object to get through)   # Private
    maxsalary = 50000                                               # Public
    _companyname = "ABC Corp."                                      # Protected

    def __init__(self, name, salary, department, bonus, overtime):               # Constructor
        self.__name = name                                                              # Instance variable (Need object to get through)
        self.__salary = salary
        self.departmet = department
        self.__bonus  = bonus
        self.__overtime = overtime
        
    def display(self):                                          # Method
        print("Employee Name = " + self.__name)                 # String == + // ,format() 
        print("Salary = ",format(self.__salary))                # Numeric == +str() // ,format() 
        print("Salary = " + str(self.__salary))
        print("Salary = {}".format(self.__salary))
        print("Department Name = ",format(self.departmet))      
        print("Department Name = {}".format(self.departmet))    # "{}".format() // "",format()

    def getIncome(self):
        return self.__salary*12 + self.__bonus + self.__overtime

    def __str__(self):
        income = self.__salary*12 + self.__bonus + self.__overtime
        return print("A={}, B={}, C={}, D={}".format(self.__name, self.departmet, self.__salary, income))


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


Em1 = Accounting("Kong", 10000, 45, 5000, 0)                                 # Object
Em2 = Programmer("Jojo", 40000, 4, "Gaming", 7500, 0)
Em3 = Sale("Nutty", 35000, "Bangkok", 2000, 500)

print("------------------Em1--------------------")
Em1.display()                                                       # Output, Print
print("*** Income Summary = {}" .format(Em1.getIncome()))       
Em1.__str__()

print("\n------------------Em2--------------------")
Em2.display()
print("*** Income Summary = {}" .format(Em2.getIncome()))
Em2.__str__()

print("\n------------------Em3--------------------")
Em3.display()
print("*** Income Summary = {}" .format(Em3.getIncome()))
Em3.__str__ ()


print("\n######################################")
print(Employee._Employee__minsalary)                               # Error because it's private variable
print(Employee.maxsalary)
print(Employee._companyname)
