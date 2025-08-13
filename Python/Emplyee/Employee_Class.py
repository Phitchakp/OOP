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