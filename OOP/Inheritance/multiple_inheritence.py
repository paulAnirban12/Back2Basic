# Multiple Inheritance Example
#  Person
#   ↑
# Student               Internship
#   ↑                      ↑
# GraduateStudent →→→→ GraduateIntern

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
        self.ID = ID
        self.Department = Department

    def get_info(self):
        super().get_info()
        print(f"ID: {self.ID}")
        print(f"Department: {self.Department}")



class GraduateStudent(Student):
    def __init__(self, name, age, gender, ID, Department, CGPA, Year_Of_Passing):
        super().__init__(name, age, gender, ID, Department)
        self.CGPA = CGPA
        self.Year_Of_Passing = Year_Of_Passing

    def get_info(self):
        super().get_info()
        print(f"CGPA: {self.CGPA}")
        print(f"Year of Passing: {self.Year_Of_Passing}")



class Internship:
    def __init__(self, company, duration):
        self.company = company
        self.duration = duration

    def get_info(self):
        print(f"Company: {self.company}")
        print(f"Duration: {self.duration}")

class GraduateIntern(GraduateStudent, Internship):
    def __init__(self, name, age, gender, ID, Department, CGPA, Year_Of_Passing, company, duration):
        GraduateStudent.__init__(self, name, age, gender, ID, Department, CGPA, Year_Of_Passing)
        Internship.__init__(self, company, duration)

    def get_info(self):
        # super() will give priority to the left-most parent in the MRO (Method Resolution Order)
        GraduateStudent.get_info(self)
        Internship.get_info(self)

# 🧪 Test
student2 = GraduateIntern('A', 24, 'Male', 191003612, 'CSE', 3.43, 2023, 'HP', 1)
student2.get_info()
