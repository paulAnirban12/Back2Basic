# Single level Inheritence
#   Person
#   ↑
# Student 
class Person:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Gender: {self.gender}")
    
class Student(Person):

    def __init__(self, name, age, gender,ID,Department):
        super().__init__(name, age, gender)
        # In this way,we can get access of the init of parent class, Person.
        self.ID = ID
        self.Department = Department

    def get_info(self):
        super().get_info()
        print(f"ID: {self.ID}")
        print(f"Department: {self.Department}")

# Multi level Inheritence
#  Person
#   ↑
# Student              
#   ↑                      
# GraduateStudent
class Graduate_Student(Student):

    def __init__(self, name, age, gender,ID,Department,CGPA,Year_Of_Passing):
        super().__init__(name, age, gender,ID,Department)
        # In this way,we can get access of the init of parent class, Student and the grandparent class, Person.
        self.CGPA = CGPA
        self.Year_Of_Passing = Year_Of_Passing

    def get_info(self):
        super().get_info()
        print(f"CGPA: {self.CGPA}")
        print(f"Year_Of_Passing: {self.Year_Of_Passing}")


# Multiple Inheritence
# # Person
#   ↑
# Student               Internship
#   ↑                      ↑
# GraduateStudent →→→→ GraduateIntern
class Internship:

    def __init__(self,company,duration):
        self.company = company
        self.duration = duration

    def get_info(self):
        
        print(f"Company: {self.company}")
        print(f"Duration: {self.duration}")

class GraduateIntern(Graduate_Student,Internship):

    def __init__(self, name, age, gender, ID, Department, CGPA, Year_Of_Passing,company,duration):
        Graduate_Student.__init__(self,name, age, gender, ID, Department, CGPA, Year_Of_Passing)
        Internship.__init__(self,company,duration)

    def get_info(self):
        super().get_info()
    # super() will always give priority to the left parent only.

# person1 = Person('A',19,'Male')
# person1.get_info()

# student1 = Student('B',16,'Female',1004105,'CSE')
# student1.get_info()

student2 = GraduateIntern('A',24,'Male',191003612,'CSE',3.43,2023,'HP',1)
student2.get_info()