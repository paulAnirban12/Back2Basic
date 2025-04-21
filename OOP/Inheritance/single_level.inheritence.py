# 📘 Single Level Inheritance
#   Person
#     ↑
#   Student 

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
        # Accesses the constructor of the parent class (Person)
        self.ID = ID
        self.Department = Department

    def get_info(self):
        super().get_info()
        print(f"ID: {self.ID}")
        print(f"Department: {self.Department}")


# 🧪 Test
student1 = Student('B', 20, 'Female', 1004105, 'CSE')
student1.get_info()
