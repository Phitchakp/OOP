class Employee:
    __minsalary = 5000
    maxsalary = 50000
    _companyname = "ABC Corp."

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.departmet = department




class Accounting(Employee):
    pass

class Programmer(Employee):
    pass

class Sale(Employee):
    pass


em1 = Accounting("Kong", 10000)
em2 = Programmer("Jojo", 40000)
em3 = Sale("Nutty", 35000)