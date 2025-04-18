class Student:

    def __init__(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def __add__(self, other):
        

        marks1 = self.marks1 + other.marks1
        marks2 = self.marks2 + other.marks2
        Student3 = Student(marks1,marks2)

        return Student3
    
    def __str__(self):
        return self.marks1, self.marks2



Student1 = Student(69,96)
Student2 = Student(89,41)

Student3 = Student1 + Student2

print(Student1.__str__())
# Can't add two Student objects directly—need to overload __add__ to define addition logic.
# To print combined marks nicely, overload __str__ as well.


# Scenario: You’re building a Bank Account system, and you want to:
# 1.Add two accounts (combine balances)
# 2.Compare accounts using > or < (based on balance)
# 3.Subtract money using -
# 4.Show account details using str() or print()

class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __add__(self,other):
        total = self.balance + other.balance
        Joint = Account("",total)
        return Joint
    
    def __gt__(self,other):
        balance1 = self.balance
        balance2 = other.balance

        if balance1>balance2:
            return True
        else:
            return False
        
    def __sub__(self,other):
        total = self.balance - other.balance
        Joint = Account("",total)
        return Joint
    
    def __str__(self):
        return f"{self.name}'s account has {self.balance}"
    

ac1 = Account("A",900000)
ac2 = Account("B",600000)

accounts = [Account("A",900000),Account("B",600000)]
for acc in accounts:
    print(acc)

combined = ac1 + ac2
print(f"Their joint account has {combined.balance}")

if ac1>ac2:
    print(f"{ac1.name} has more money than {ac2.name}")
    difference = ac1 - ac2
else:
    print(f"{ac2.name} has more money than {ac1.name}")
    difference = ac2 - ac1
print(f"The difference of their account is {difference.balance}")


