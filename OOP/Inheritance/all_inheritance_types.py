
# 🧬 Inheritance Type           | 🧱 Classes and Relationships
# -----------------------------|-----------------------------------------------------
# Single Inheritance           | Person → Teacher
# Multilevel Inheritance       | Person → Teacher → MathTeacher
# Hierarchical Inheritance     | Person → Teacher, Student, Administrator
# Multiple Inheritance         | Teacher, Student → ClassRepresentative

# ✅ Class Structure Overview:
# Class: Person                | Attr: _name, _age, _gender        | Method: display_info()
# Class: Teacher               | Attr: subject, experience      | Method: teach()
# Class: MathTeacher           | Attr: specialization           | Method: conduct_exam()
# Class: Student               | Attr: grade_level, subjects    | Method: study()
# Class: Administrator         | Attr: department, role         | Method: assign_homework()
# Class: ClassRepresentative   | Attr: leadership_skills       | Method: organize_meeting()

# Method Logic:
# Person: display_info()         # Displays person's info (_name, _age, _gender)
# Teacher: teach()               # Displays subject taught & experience
# MathTeacher: conduct_exam()    # Simulates conducting an exam
# Student: study()               # Displays subjects & study hours
# Administrator: assign_homework() # Prints homework details & deadlines
# ClassRepresentative: organize_meeting() # Prints meeting details (time, _agenda, date)

# 📦 Import required modules
from datetime import datetime, timedelta, date
import random

# 🧩 Base Class: Person
class Person:
    # 🔥 Class variables for tracking all persons
    students = []
    teachers = []
    admins = []

    def __init__(self, _name, _age, _gender):
        # 🏷️ Attributes common to all persons
        self._name = _name
        self._age = _age
        self._gender = _gender
        print(f"{self._name}'s information got registered")

    def display_info(self):
        # 📄 Display basic person info
        print(f"""Name:{self._name}
Age:{self._age}
Gender:{self._gender}""")

# 📚 Derived Class: Teacher (Single Inheritance)
class Teacher(Person):
    def __init__(self, _name, _age, _gender, subject, experience):
        # 👨‍🏫 Initialize parent class attributes
        Person.__init__(self, _name, _age, _gender)
        # 🎯 Specific attributes for Teacher
        self_id = random.randint(100000, 999999)
        self.role = "Teacher"
        self.subject = subject
        self.experience = experience
        Person.teachers.append(self)

    def teach(self):
        # 🗣️ Display teaching-related info
        super().display_info()
        print(f"""A {self.subject} {self.role} 
Experience: {self.experience} years""")

# 📚 Multilevel Inheritance: MathTeacher → Teacher → Person
class MathTeacher(Teacher):
    def __init__(self, _name, _age, _gender, subject, experience, specialization):
        # 🧮 Initialize Teacher first
        super().__init__(_name, _age, _gender, subject, experience)
        self.specialization = specialization
        Person.teachers.append(self)

    def conduct_exam(self):
        # 📝 Conducting exam (with current date)
        date_now = datetime.now().strftime("%B %d, %Y")
        super().display_info()
        super().teach()
        print(f"Conducting Exam: {self.specialization}, Date: {date_now}")

# 🎓 Derived Class: Student (Hierarchical Inheritance)
class Student(Person):
    def __init__(self, _name, _age, _gender, subjects, phase):
        # 📖 Initialize base person info
        Person.__init__(self, _name, _age, _gender)
        # 🧩 Student-specific attributes
        self.id = random.randint(100000, 999999)
        self.role = "Student"
        self.subjects = subjects
        self.phase = phase
        
        # 🕒 Study time calculation based on phase
        total_subjects = len(self.subjects)
        if total_subjects != 0:
            if phase == "Exam":
                self.study_time = 12 // total_subjects
            else:
                self.study_time = 8 // total_subjects
        else:
            print(f"There is no need of hurry as {_name} has lots of time to be serious.")
            self.study_time = 0

        Person.students.append(self)

    def study(self):
        # 📚 Show study plan
        print(f"Id:{self.id}")
        super().display_info()
        if self.subjects == None:
            print(f"""A {self.role} 
No need to take stress as {self._name} has no subjects this time. SO, Relax.""")
        else:
            if self.phase == "Regular":
                print(f"""A {self.role} 
{self._name} has subjects like {self.subjects} this time. As exam time is far, No need to take stress.
SO, Relax""")
            else:
                print(f"""A {self.role} 
Subjects: {self.subjects}
Study time for each subject: Daily {self.study_time} hours""")

# 🏛️ Derived Class: Administrator (Hierarchical Inheritance)
class Administrator(Person):
    def __init__(self, _name, _age, _gender, department, role):
        # 🏢 Initialize parent class and set department/role
        super().__init__(_name, _age, _gender)
        self.department = department
        self.role = role

    def assign_homework(self, subject, chapter, deadline):
        # 📝 Assign homework with deadline
        print(f"""Assigning Homework: {subject} {chapter}
Deadline: {deadline}""")

    def correctify_info(self, student_id, new__name, new__age, alloted_subjects):
        # 🔒 Admin can correct student info
        if self.role.lower() not in ["head admin", "admin"]:
            print("Confidential Information. Not accessible for you.")
            exit()
        else:
            for student in Person.students:
                if student.id == student_id:
                    print("--Before Update---")
                    student.study()
                    # ✍️ Update attributes if provided
                    if new__name is not None:
                        student._name = new__name
                    if new__age != 0:
                        student._age = new__age
                    if len(alloted_subjects) != 0:
                        student.subjects = alloted_subjects
            print("------After Update------")
            student.study()

# 👑 Derived Class: ClassRepresentative (Multiple Inheritance)
class ClassRepresentative(Teacher, Student):
    def __init__(self, _name, _age, _gender, subject, experience, subjects, phase, leadership_skills):
        # 🛠️ MRO: Initialize Teacher first
        super().__init__(_name, _age, _gender, subject, experience)
        # 🛠️ Manually Initialize Student
        Student.__init__(self, _name, _age, _gender, subjects, phase)
        self.leadership_skills = leadership_skills

    def organize_meeting(self, agenda, date, time):
        # 🗓️ Organize a meeting
        Teacher.display_info(self)
        Student.display_info(self)
        if self.leadership_skills:
            if self._gender != "Female":
                print(f"""{self._name} has leadership skills as he {agenda} on {date} at {time}""")
            else:
                print(f"""{self._name} has leadership skills as she {agenda} on {date} at {time}""")
        else:
            print(f"{self._name} has no leadership skills.")

# --------------------------------------------------------------------
# 🎯 Test cases to verify the structure

# Example: Person object
# Creating an instance of Person with name, age, and gender
Person1 = Person("A", 25, "Male")
# Displaying person information
Person1.display_info()

# Test case for Teacher class
# Creating an instance of Teacher with name, age, gender, specialization, and experience
teacher = Teacher("John Doe", 30, "Male", "English", 7)
# Teacher teaches the subject
teacher.teach()

# Test case for MathTeacher class
# Creating an instance of MathTeacher with specialization in Algebra and Geometry
teacher2 = MathTeacher("Xavier", 24, "Male", "Math", 4, "Algebra and Geometry")
# MathTeacher conducts an exam
teacher2.conduct_exam()

# List to store valid subject names
subjects = []  

# Input loop for valid subject names
while True:
    subject_name = input("Please enter the subject name: ")
    
    # Check if the input is a valid non-empty string (alphabetical characters only)
    if subject_name.isalpha() and subject_name.strip() != "":
        subjects.append(subject_name)  # Add valid subject to the list
    else:
        print("Invalid input! Exiting...")
        break  # Exit the loop if invalid input is given

# Print the list of valid subjects and create a student instance
total_subject = len(subjects)
student = Student("Xavier", 24, "Male", subjects, "Regular", total_subject)
# Student starts studying
student.study()

# Creating an instance of Teacher
teacher = Teacher("John Doe", 30, "Male", "English", 7)
# Teacher teaches the subject
teacher.teach()

# Creating an Administrator instance for homework assignment
admin1 = Administrator("Ms.Y", 40, "Female", "Academic Affairs", "Coordinator")

# Assign homework with subject, chapter, and deadline
subject = teacher.subject
deadline = date.today() + timedelta(days=7)
deadline = deadline.strftime("%B %d, %Y")
chapter = input("Enter topic for homework:")
admin1.assign_homework(subject, chapter, deadline)

# Creating another Administrator and correcting student info
admin2 = Administrator("Arif", 45, "Male", "Admin Office", "Head Admin")
student1 = Student("Xavier", 24, "Male", "None", "Regular")
id = student1.id
new_name = "Paul"
_age = 20
subjects = ["History", "Math", "Geography"]
# Student starts studying
student1.study()
# Admin corrects student info
admin2.correctify_info(id, new_name, _age, subjects)

# Example: ClassRepresentative object
# Creating a ClassRepresentative with subjects and exam-related details
subjects = ["Data Structure", "Operating System", "Electrical Circuits"]
CR1 = ClassRepresentative("M", 26, "Female", "ComputerScience", 0, subjects, "Exam", True)

# Meeting details: Setting a future meeting date
meeting_date = date.today() + timedelta(days=3)
time_now = datetime.now().strftime("%I:%M %p")

# 📢 Organize a meeting: Class representative organizes a meeting for an upcoming school event
CR1.organize_meeting("Organizes Class Meeting to Discuss upcoming school event", meeting_date, time_now)


# Example: ClassRepresentative object
subjects = ["Data Structure", "Operating System", "Electrical Circuits"]
CR1 = ClassRepresentative("M", 26, "Female", "ComputerScience", 0, subjects, "Exam", True)

# Meeting details
meeting_date = date.today() + timedelta(days=3)
time_now = datetime.now().strftime("%I:%M %p")

# 📢 Organize a meeting
CR1.organize_meeting("organizes Class Meeting to Discuss upcoming school event", meeting_date, time_now)
