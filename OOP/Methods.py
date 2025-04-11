# Any method with self, which means works with objects, is instance method. Always have to use self
# Class method always use cls instead of self.
# If we don't use @classmethod, we need to pass cls while calling the method. If you don't want to do it, just use @classmethod just above the class method.@classmethod is a decorator
#Get method:Accessors cause we get access in Get method
# Set method:Mutators as we can modify in Set method
# Static Method: Does not care about whether anything is instance or class.
# We have to use @staticmethod just above the static method.@staticmethod is a decorator

class Students:

    classroom = "4B"
    def __init__(self,marks1,marks2,marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def avg(self):
    #   instance method
      average = (self.marks1+self.marks2+self.marks3)/3
      print(f"Average: {average:.2f}") 

    def get_marks1(self):
    #    Accessor
       print(f"{self.marks1}")

    def set_marks1(self,marks):
    #    Mutator
       self.marks1 = marks
    
    @classmethod
    def GetClassroom(cls):
    #    Class method
        print(f"{cls.classroom}")
    
    @staticmethod
    def info():
       print("Welcome to ABC School.")

student1 = Students(65,25,89)
student2 = Students(95,89,2)

student1.avg()

student1.set_marks1(98)
student1.get_marks1()
student1.avg()

Students.GetClassroom()
Students.info()