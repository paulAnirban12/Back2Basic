# -------------------------------
# 👨‍🎓 Base Class: Person
# -------------------------------
# Purpose: Acts as a parent class for all types of people in the system
# Attributes:
#   - _name: (protected) common to all, accessible in subclasses
#   - __email: (private) only accessible via getter and setter (encapsulation)
#   - _role: (protected) indicates the type of user ("Student", "Teacher", etc.)
# Methods:
#   - __init__(self, name, email, role): Initializes all the attributes
#   - get_email(self): Returns the private email (encapsulation - getter)
#   - set_email(self, new_email): Validates and sets new email (encapsulation - setter with logic)
#   - get_info(self): Returns basic info — to be overridden by subclasses
from dataclasses import dataclass
@dataclass
class Person:
    _name:str
    __email:str
    _role:str
    def __post_init__(self):print(f"{self._name}'s information has been added.")
    @property
    def email(self):return self.__email
    @email.setter
    def email(self,new_email):
        if '@' in new_email:
            self.__email = new_email
            print(f"{self._name}'s email has been updated.")
        else:raise ValueError("Invalid Email Address")
    def get_info(self):
        print(f"Name: {self._name}, Role: {self._role}")
# -------------------------------
# 👩‍🎓 Derived Class: Student (Single Inheritance from Person)
# -------------------------------
# Purpose: Represents a student enrolled in the university
# Attributes:
#   - _student_id: (protected) Unique ID for student
#   - _courses: (protected list) Keeps track of enrolled courses
# Methods:
#   - enroll_course(self, course): Adds a course to the _courses list
#   - get_info(self): Overrides Person's get_info method 
#                     (Polymorphism — Method Overriding) to show student-specific details
# 🔄 Operator Overloading: __add__ in Student class
# -------------------------------
# Purpose: Allows merging two Student objects
# How:
#   - student1 + student2 returns a new Student with combined courses
#     (Polymorphism — Operator Overloading)
@dataclass
class Student(Person):
    _student_id:str
    _courses:list[str]
    def enroll_course(self, course):
        if course not in self._courses:
            self._courses.append(course)
            print(f"""{course} has been added in {self._name}'s course list.
Now {self._name} has {len(self._courses)} courses.""")
        else:
            raise ValueError(f"{course} is already in {self._name}'s course list.")
    def get_info(self):
        print(f"""Name:{self._name}
Id:{self._student_id}
Courses:{sorted(self._courses)}""")
    def __add__(self,other):
        return self._courses + other._courses

student1 = Student("AK","Ak@gmail.com","Student","SC122025",["History","Math"])
student1.email = "SC122025@gmail.com"
print(student1.email)
student1.enroll_course("Algebra")
student1.get_info()
student2 = Student("AP","AP@gmail.com","Student","SC2564",["Geography"])
student3_subjects = sorted(student1.__add__(student2))

student3 = Student("ANK","ANk@gmail.com","Student","SC122035",student3_subjects)
student3.get_info()
# -------------------------------
# 👨‍🏫 Derived Class: Teacher (Single Inheritance from Person)
# -------------------------------
# Purpose: Represents a faculty member
# Attributes:
#   - _employee_id: (protected) Unique ID for teacher
#   - _subjects: (protected list) Subjects they teach
# Methods:
#   - assign_subject(self, subject): Adds subject to list
#   - get_info(self): Overrides Person's get_info (Polymorphism again)
@dataclass
class Teacher(Person):
    _employee_id:str
    _subjects:list[str]
    def assign_subject(self, subject):
        if subject not in self._subjects:
            self._subjects.append(subject)
            print(f"""{subject} has been added in {self._name}'s subject list.
Now {self._name} has {len(self._subjects)} subjects to teach.""")
        else:
            raise ValueError(f"{subject} is already in {self._name}'s subject list.")
    def get_info(self):
        if len(self._subjects) == 0:
            print(f"""Name:{self._name}
{self._name} was not assigned any subject.""")
        else:
            print(f"""Name:{self._name}
Subjects:{sorted(self._subjects)}""")
# Teacher1 = Teacher("ANP","ANP@gmail.com","Teacher","ANP2210",["Math","Algebra"])
# Teacher1.assign_subject("Calculus")
# Teacher1.get_info()
# -------------------------------
# 🔁 Multiple Inheritance: Admin (inherits from Student and Teacher)
# -------------------------------
# Purpose: Admins may take courses and teach — hence, inherits both roles
# Attributes:
#   - _admin_level: (protected) Specifies clearance or privileges
# Methods:
#   - get_info(self): Overrides again to merge info from both Student and Teacher
#     Demonstrates multiple inheritance and Method Resolution Order (MRO)
@dataclass
class Admin(Student,Teacher):
    _admin_level:str
    def get_info(self):
        super().get_info()
        Teacher.get_info(self)
        print(f"Admin Level:{self._admin_level}")
# admin1 = Admin("AP","AP@gmail.com","Admin","AP2564",[],"SC2564",["History","Geography"],"FrontDesk")
# admin1.get_info()
# admin1.assign_subject("Basic Mathematics")
# admin1.get_info()
# -------------------------------
# 🔗 Multilevel Inheritance: ResearchStudent (inherits from Student)
# -------------------------------
# Purpose: Represents a student engaged in research
# Attributes:
#   - _thesis_topic: (protected) Describes research area
# Methods:
#   - get_info(self): Extends Student’s version to include thesis
@dataclass
class ResearchStudent(Student):
    _thesis_topic:str
    def get_info(self):
        super().get_info()
        print(f"Thesis Topic:{self._thesis_topic}")
# student1 = Student("AK","Ak@gmail.com","Student","SC122025",["History","Math"])
# ResearchStudent1 = ResearchStudent(student1._name,student1.email,student1._role,student1._student_id,student1._courses,"Phishing detection")
# ResearchStudent1.get_info()
# -------------------------------
# 🧩 Abstract Base Class: CourseManager
# -------------------------------
# Purpose: Defines an interface for course management actions
# Type: Abstract Base Class (Abstraction)
# Methods (abstract):
#   - add_course(self, course): Must be implemented to add a course
#   - remove_course(self, course): Must be implemented to remove a course
from abc import ABC
class CourseManager(ABC):
    @classmethod
    def add_course(self, course):pass
    def remove_course(self, course):pass

# -------------------------------
# 🧑‍💼 Derived Class: AdminStaff (inherits from CourseManager)
# -------------------------------
# Purpose: Implements course management
# Attributes:
#   - _managed_courses: (protected list) List of managed courses
# Methods:
#   - add_course(self, course): Implements course addition
#   - remove_course(self, course): Implements course removal
#   - generate_report(self, type="summary"): Simulates Method Overloading
@dataclass
class AdminStaff(CourseManager):
    _managed_courses:list[str]
    def add_course(self, course):
        if course not in self._managed_courses:
            self._managed_courses.append(course)
            print(f"""{course} has been added to the courselist.
Now the courses available:{sorted(self._managed_courses)}""")
        else:raise ValueError("Course already there.")
    def remove_course(self, course):
        if course not in self._managed_courses:raise ValueError("Course not there.")
        else:
            self._managed_courses.remove(course)
            print(f"""{course} has been removed from the courselist.
Now the courses available:{sorted(self._managed_courses)}""")
# AdminStaff1 = AdminStaff(["History","Geography"])           
# AdminStaff1.add_course("Mathematics")
# AdminStaff1.remove_course("History")
# -------------------------------
# 🛠️ Utility Class: UniversityUtility
# -------------------------------
# Purpose: Demonstrates Duck Typing and Method Overloading concepts
# Methods:
#   - print_info(self, obj): Accepts any object and calls obj.get_info() (Duck Typing)
#   - add(self, *args): Returns sum of arguments (Method Overloading with *args)
class UniversityUtility:
    def print_info(self, obj):obj.get_info()
    def add(self,*args):
        result = 0
        for val in args:result += val
        print(result)
utility = UniversityUtility()
# Teacher1 = Teacher("ANP","ANP@gmail.com","Teacher","ANP2210",["Math","Algebra"])
# utility.print_info(Teacher1)
# student1 = Student("AK","Ak@gmail.com","Student","SC122025",["History","Math"])
# student1_subjects = len(student1._courses)
# admin1 = Admin("AP","AP@gmail.com","Admin","AP2564",[],"SC2564",["History","Geography"],"FrontDesk")
# admin1_subjects = len(admin1._courses)
# utility.add(student1_subjects,admin1_subjects)
# -------------------------------



# -------------------------------
# 🔐 Encapsulation Summary:
# -------------------------------
# - __email in Person is private: Accessible only via get_email/set_email
# - set_email includes validation: prevents setting invalid email addresses
# - Protects internal state from direct access/modification


# -------------------------------
# 🧠 Polymorphism Summary:
# -------------------------------
# - Method Overriding: get_info() is redefined in each subclass
# - Operator Overloading: __add__ allows + operation on students
# - Duck Typing: print_info(obj) works for any object with get_info()
# - Method Overloading: add(*args) simulates different signatures


# -------------------------------
# 🏗️ Inheritance Summary:
# -------------------------------
# - Single: Student → Person, Teacher → Person
# - Multiple: Admin → Student + Teacher
# - Multilevel: Person → Student → ResearchStudent
# - Abstract: CourseManager → AdminStaff


# ✅ This design demonstrates all four pillars of OOP — clearly separated but functionally connected.
# Highly reusable, easy to extend, and fits well in a real-world Python project.
