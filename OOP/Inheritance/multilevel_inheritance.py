# Multi level Inheritance
#  Person
#   ↑
# Student              
#   ↑                      
# GraduateStudent

class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Gender: {self.gender}")
    
class Student(Person):

    def __init__(self, name, age, gender, ID, Department):
        super().__init__(name, age, gender)
        # In this way, we can get access to the init of the parent class, Person.
        self.ID = ID
        self.Department = Department

    def get_info(self):
        super().get_info()
        print(f"ID: {self.ID}")
        print(f"Department: {self.Department}")



class Graduate_Student(Student):

    def __init__(self, name, age, gender, ID, Department, CGPA, Year_Of_Passing):
        super().__init__(name, age, gender, ID, Department)
        # In this way, we can get access to the init of parent class, Student, and the grandparent class, Person.
        self.CGPA = CGPA
        self.Year_Of_Passing = Year_Of_Passing

    def get_info(self):
        super().get_info()
        print(f"CGPA: {self.CGPA}")
        print(f"Year_Of_Passing: {self.Year_Of_Passing}")

# 🧪 Test
student2 = Graduate_Student('A', 24, 'Male', 191003612, 'CSE', 3.43, 2023)
student2.get_info()
