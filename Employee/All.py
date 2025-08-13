class Employee:                                                 # Encapsulation     # Class
    __minsalary = 5000                                          # Attribute, Proporty   # Class variable (no need object to get through)   # Private
    maxsalary = 50000                                               # Public
    _companyname = "ABC Corp."                                      # Protected

    def __init__(self, name, salary, department):               # Constructor
        self.__name = name                                                              # Instance variable (Need object to get through)
        self.__salary = salary
        self.departmet = department
        
    def display(self):                                          # Method
        print("Employee Name = " + self.__name)                 # String == + // ,format() 
        print("Salary = ",format(self.__salary))                # Numeric == +str() // ,format() 
        print("Salary = " + str(self.__salary))
        print("Salary = {}".format(self.__salary))
        print("Department Name = ",format(self.departmet))      
        print("Department Name = {}".format(self.departmet))    # "{}".format() // "",format()

    def getIncome(self, bonus=0, overtime=0):
        return self.__salary*12 + bonus + overtime

    # def __str__(self, bonus=0, overtime=0):
    #     return "A={}, B={}, C={}, D={}".format(self.__name, self.departmet, self.__salary, self.getIncome())

    def __str__(self, bonus=0, overtime=0):
        income = self.__salary*12 + bonus + overtime
        return print("A={}, B={}, C={}, D={}".format(self.__name, self.departmet, self.__salary, income))


class Accounting(Employee):                                     # Inheritance       # Subclass
    department = "Accounting"

    def __init__(self, name, salary, age):                      # Polymorphism 1
        super().__init__(name, salary, self.department)         # Super
        self.__age = age

    def display(self):                                          # Polymorphism 2
        super().display()
        print("Age =", format(self.__age))

    def __str__(self):
        return print(super().__str__() ,", Age = {}" .format(self.__age))


class Programmer(Employee):
    department = "Programmer"

    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.department)
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

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.department)
        self.area = area

    def display(self):
        super().display()
        print("Area, Zone =" + self.area)
    
    def __str__(self):
        return print(super().__str__() ,", Area = {}" .format(self.area))


Em1 = Accounting("Kong", 10000, 45)                                 # Object
Em2 = Programmer("Jojo", 40000, 4, "Gaming")
Em3 = Sale("Nutty", 35000, "Bangkok")

print("------------------Em1--------------------")
Em1.display()                                                       # Output, Print
print("*** Income Summary = {}" .format(Em1.getIncome(5000, 0)))       
Em1.__str__()                                                       # String output

print("\n------------------Em2--------------------")
Em2.display()
print("*** Income Summary = {}" .format(Em2.getIncome(7500, 0)))
Em2.__str__()

print("\n------------------Em3--------------------")
Em3.display()
print("*** Income Summary = {}" .format(Em3.getIncome(2000, 500)))
Em3.__str__ ()


print("\n######################################")
print(Employee._Employee__minsalary)                               # Error because it's private variable
print(Employee.maxsalary)
print(Employee._companyname)
