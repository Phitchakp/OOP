# Overloading
class Employee:
    #class variable
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"
    def __init__(self,name,salary,department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

    #แสดงรายละเอียด
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)

    #รายได้ต่อปี
    def _getIncome(self,bonus=0,overtime=0):
        return (self.__salary *12)+bonus+overtime

    def __str__(self):
        return ("ขื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {}".format(self.__name,self._department,self.__salary))
    
class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.__age = age
    
    def _showData(self):
        super()._showData()
        print("อายุ = "+str(self.__age))
        print("###############")
    
    def __str__(self):
        return (super().__str__()+" , อายุ = {} ปี".format(self.__age))


class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = "+str(self.__exp))
        print("ทักษะ = "+self.__skill)
        print("###############")
    
    def __str__(self):
        return (super().__str__()+" , ประสบการณ์ = {} ปี, ทักษะ = {}".format(self.__exp,self.__skill))


class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = "+self.__area)
        print("###############")
    
    def __str__(self):
        return (super().__str__()+" , พื้นที่รับผิดชอบ = {}".format(self.__area))


account = Accounting("ก้อง",10000,30)
print("บัญชี รายได้ต่อปี = "+str(account._getIncome(3000)))
print(account.__str__())

programmer = Programmer("โจโจ้",40000,2,"พัฒนาเกม")
print("โปรแกรมเมอร์ รายได้ต่อปี = "+str(programmer._getIncome(10000,500)))

sale = Sale("นัท",35000,"เชียงใหม่")
print("ฝ่านขาย รายได้ต่อปี = "+str(sale._getIncome()))
