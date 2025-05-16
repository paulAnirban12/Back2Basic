# 🚀 Step 1: Traditional Class without @dataclass
# ------------------------------------------------
# ❌ Problem: Manually defining __init__() becomes repetitive (boilerplate code).
# Each attribute must be manually assigned inside the constructor.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    

# Creating object
student1 = Student("Arif", 20, "A")
print(student1.name, student1.age, student1.grade)

# 🚀 Step 2: Using @dataclass for Cleaner Code
# ------------------------------------------------
# ✅ Solution: @dataclass automatically generates:
#    - __init__() method
#    - __repr__() method
#    - __eq__() method
# You only need to declare attributes with their types.
# Code becomes much cleaner, easier to maintain and update.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: str

    def __post_init_(self):
        print(f"{self.name}'s information has been registered!")

# Creating object
student1 = Student("Arif", 20, "A")
print(student1.name, student1.age, student1.grade)
