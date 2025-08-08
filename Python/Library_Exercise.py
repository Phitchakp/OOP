from datetime import date, timedelta


class Book:
    def __init__(self, title, author, ISBN, amount):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.amount = amount
        self.isAvailable = amount > 0

    def checkAvailability(self):
        return self.amount > 0

    def borrow(self):
        if self.checkAvailability():
            self.amount -= 1
            self.isAvailable = self.amount > 0
            return True
        return False

    def returnBook(self):
        self.amount += 1
        self.isAvailable = True
        
    # def getbook(self):
    #     return self.title




class Loan:
    def __init__(self, loanid, issueDate, dueDate, returnedDate=None):
        self.loanid = loanid
        self.issueDate = issueDate
        self.dueDate = dueDate
        self.returnedDate = returnedDate
        self.status = "Open" if returnedDate is None else "Closed"



class person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def calculateFine(self, loan):
        if loan.returnedDate and loan.returnedDate > loan.dueDate:
            pay_fine = (loan.returnedDate - loan.dueDate).days
            return pay_fine * 1.0  # $1 per day fine
        return 0.0
   
class member(person):
    def __init__(self, name, address, phone, memberid):
        super().__init__(name, address, phone)
        self.memberid = memberid

class staff(person):
    def __init__(self, name, address, phone, staffid):
        super().__init__(name, address, phone)
        self.staffid = staffid

    def calculateFine(self, loan):
        return 0.0



# Loan due 5 days ago, returned today (5 days late)
late_loan = Loan(
    loanid="L001",
    issueDate=date(2025, 6, 20),
    dueDate=date(2025, 7, 9),
    returnedDate=date(2025, 7, 14)
)

# Create a Member and Staff
p1 = member(memberid="M001", name="Alice")
p2 = staff(staffid="S001", name="Bob")

# Calculate fines
print(f"{member.name} (Member) fine: ${member.calculateFine(late_loan)}")
print(f"{staff.name} (Staff) fine: ${staff.calculateFine(late_loan)}")
