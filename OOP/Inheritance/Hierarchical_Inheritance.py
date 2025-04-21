# Hierarchical Inheritance Example
#         Person  
#        ↗   ↑   ↖  
#  Student  Teacher  Administrator
#
# All (Student, Teacher, Administrator) inherit common traits (name, age, address) from Person.
# But each has unique roles:
# - Student → grades, courses
# - Teacher → subjects, schedule
# - Administrator → manages operations, staff
# 🎯 Same base (Person), different behaviors.

class Person:

    def __init__(self, name, age, gender,role):
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
    
    def get_info(self):
        print(f"---Information of a {self.role}---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Gender: {self.gender}")
        
    
class Student(Person):

    def __init__(self, name, age, gender, role, ID, Department):
        super().__init__(name, age, gender,role)
        # Accesses the constructor of the parent class (Person)
        self.ID = ID
        self.Department = Department

    def get_info(self):
        super().get_info()
        print(f"ID: {self.ID}")
        print(f"Department: {self.Department}")

class Teacher(Person):

    def __init__(self, name, age, gender, role, Subject):
        super().__init__(name, age, gender,role)
        # Accesses the constructor of the parent class (Person)Subject
        self.Subject = Subject

    def get_info(self):
        super().get_info()
        print(f"Subject: {self.Subject}")

class Administrator(Person):

    def __init__(self, name, age, gender,role,Employee_id,Office_location):
        super().__init__(name, age, gender, role)
        # Accesses the constructor of the parent class (Person)
        self.Employee_id = Employee_id
        self.Office_location = Office_location

    def get_info(self):
        super().get_info()
        print(f"Employee_id: {self.Employee_id}")
        print(f"Office_location: {self.Office_location}")

employee1 = Student('XOXO', 16, 'Male', 'Student', 1004105, 'CSE')
employee1.get_info()

employee2 = Teacher('B', 20, 'Female','Teacher','Algorithms')
employee2.get_info()

employee3 = Administrator('D', 30, 'Male','Officer','A654','Admin Block')
employee3.get_info()



