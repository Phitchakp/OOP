from datetime import date, timedelta

# --- Base Classes ---
class Loan:
    def __init__(self, loanId, issueDate, dueDate, returnedDate=None):
        self.loanId = loanId
        self.issueDate = issueDate
        self.dueDate = dueDate
        self.returnedDate = returnedDate

class Person:
    def __init__(self, name):
        self.name = name

    def calculateFine(self, loan):
        if loan.returnedDate and loan.returnedDate > loan.dueDate:
            days_late = (loan.returnedDate - loan.dueDate).days
            return days_late * 1.0  # $1 per day
        return 0.0

class Member(Person):
    def __init__(self, memberId, name):
        super().__init__(name)
        self.memberId = memberId

class Staff(Person):
    def __init__(self, staffId, name):
        super().__init__(name)
        self.staffId = staffId

    def calculateFine(self, loan):
        return 0.0  # Staff pays no fines


# Loan due 5 days ago, returned today (5 days late)
late_loan = Loan(
    loanId="L001",
    issueDate=date(2025, 6, 20),
    dueDate=date(2025, 7, 9),
    returnedDate=date(2025, 7, 14)
)

# Create a Member and Staff
member = Member(memberId="M001", name="Alice")
staff = Staff(staffId="S001", name="Bob")

# Calculate fines
print(f"{member.name} (Member) fine: ${member.calculateFine(late_loan)}")
print(f"{staff.name} (Staff) fine: ${staff.calculateFine(late_loan)}")
