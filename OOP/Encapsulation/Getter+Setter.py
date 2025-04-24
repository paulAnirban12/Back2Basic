# 🔁 Getters & Setters in Python
# ------------------------------
# ✅ Concept:
# Used to access and update private attributes safely.

# 🧩 Syntax:
#   Getter (read)             |   Setter (write/update)
#   ------------------------- | ---------------------------
#   @property                 |   @<attribute>.setter
#   def get_method(self):     |   def set_method(self, val):
#       return self.__attr    |       self.__attr = val

# ✅ Notes:
# - Getter: Read-only access to private data.
# - Setter: Controls and validates updates to private data.
# - Encourages encapsulation and clean API usage.


# 🧾 Scenario: Book
# +-----------------------------+
# |        Book Object          |
# +-----------------------------+
# | - __title                  |  ← Private attribute
# | - __author                 |  ← Private attribute
# +-----------------------------+
# | + get_title()              |  ← Getter (Read title)
# | + set_title(new_title)     |  ← Setter (Update title)
# | + get_author()             |  ← Getter (Read author)
# | + set_author(new_author)   |  ← Setter (Update author)
# +-----------------------------+


class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):  # ✔️ Should match the property name: title
        self.__title = new_title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):  # ✔️ Should match the property name: author
        self.__author = new_author

# Testing
book1 = Book("Final_Countdown", "Jack Willy")
book2 = Book("Kingdom", "Tony Stark")

book2.title = "IronMan"          # ✔️ Uses the setter
print(book2.title)               # Output: IronMan

book1.author = "John Cena"       # ✔️ Uses the setter
print(book1.author)              # Output: John Cena


# 🎓 Student Record Scenario
# ---------------------------------------------------
# Attributes                     | Methods
# ----------------------------- | -----------------------------------------------
# student_name                   | get_student_name() – Get the student's name
# student_id                     | set_student_name(new_name) – Set a new name
# student_grade                  | get_student_id() – Get the student ID
#                                | set_student_id(new_id) – Set a new ID
#                                | get_student_grade() – Get the student's grade
#                                | set_student_grade(new_grade) – Set a new grade


class Student:
    def __init__(self, student_name, student_id, student_grade):
        self.__student_name = student_name  # ✔️ Private attribute for student's name
        self.__student_id = student_id      # ✔️ Private attribute for student's ID
        self.__student_grade = student_grade  # ✔️ Private attribute for student's grade

    @property
    def student_name(self):
        return self.__student_name  # ✔️ Getter for student's name
    
    @student_name.setter
    def student_name(self, new_name):  # ✔️ Setter to update student's name
        self.__student_name = new_name

    @property
    def student_id(self):
        return self.__student_id  # ✔️ Getter for student's ID
    
    @student_id.setter
    def student_id(self, new_id):  # ✔️ Setter to update student's ID
        self.__student_id = new_id

    @property
    def student_grade(self):
        return self.__student_grade  # ✔️ Getter for student's grade
    
    @student_grade.setter
    def student_grade(self, new_grade):  # ✔️ Setter to update student's grade
        self.__student_grade = new_grade

# Testing
student1 = Student("Alice", "S101", 85)  # ✔️ Create a student with name "Alice", ID "S101", and grade 85
student2 = Student("Bob", "S102", 92)    # ✔️ Create a student with name "Bob", ID "S102", and grade 92
student3 = Student("Anirban", "S103", 79)  # ✔️ Create a student with name "Anirban", ID "S103", and grade 79

# Changing the student's name using the setter
student2.student_name = "Steve"  # ✔️ Updates the student's name to "Steve"
print(student2.student_name)     # Output: Steve

# Changing the student's ID using the setter
student1.student_id = "S105"     # ✔️ Updates the student's ID to "S105"
print(student1.student_id)       # Output: S105

# Changing the student's grade using the setter
student3.student_grade = 97      # ✔️ Updates the student's grade to 97
print(student3.student_grade)    # Output: 97


# ✅ If you want role-based access control, use a custom method like set_name(faculty, new_name)

# ❌ Don’t mix @property.setter with extra arguments like faculty

# ✅ Use @property only when you want clean attribute-style access without permissions

    
