from Employee_Class import Employee
from Accounting_Class import Accounting
from Programmer_Class import Programmer
from Sale_Class import Sale


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