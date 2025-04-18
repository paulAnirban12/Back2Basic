# basic level
# Imagine you say "draw" to your toys.

# The robot draws with a pen,

# The dinosaur draws with its tail,

# The fairy draws with magic!

# Even though you said the same word—"draw"—each toy does it in its own special way.
# That’s called polymorphism in programming!

#  Here’s a fun and simple code version of that toy example using polymorphism.

class Robot():

    def draw(self):
        print("The robot draws with a pen")
    
class Dinosaur():

    def draw(self):
        print("The dinosaur draws with its tail")

class Fairy():

    def draw(self):
        print("The fairy draws with magic")

def make_toy_draw(toy):
    toy.draw()

make_toy_draw(Robot())
make_toy_draw(Dinosaur())
make_toy_draw(Fairy())



# # Advanced level
class Student:

    def __init__(self,name,Id):
        self.name = name
        self.Id = Id

    def get_id_card_info(self):
        print(f"Name:{self.name}")
        print(f"Id:{self.Id}")

class Teacher:

    def __init__(self,name,Position,Department):
        self.name = name
        self.Position = Position
        self.Department = Department

    def get_id_card_info(self):
        print(f"Name:{self.name}")
        print(f"Position:{self.Position}")
        print(f"Department:{self.Department}")

class Staff:

    def __init__(self,name,Id):
        self.name = name
        self.Id = Id
    
    def get_id_card_info(self):
        print(f"Name:{self.name}")
        print(f"Id:{self.Id}")

def print_Id_Card(person):

    person.get_id_card_info()

print_Id_Card(Student("A",100565))
print_Id_Card(Teacher("Anirban","Lecturer","Math"))
print_Id_Card(Staff("X",25))

# ✅ Is it **Duck Typing**?

# **Yes.**  
# You're passing different types of objects (`Student`, `Teacher`, `Staff`) into the same function `print_Id_Card()`, and it calls the `get_id_card_info()` method on each one **without checking their type**.

# Duck typing works like this:
# > If the object has a `get_id_card_info()` method, use it.

# And that’s exactly what your code does. So ✔️ duck typing is being used.

# ---

# ### ✅ Is it **Polymorphism**?

# **Also yes.**  
# This is **runtime polymorphism**—specifically, **method polymorphism**—because the same method name (`get_id_card_info`) behaves **differently** depending on which class the object belongs to.

# Each class implements its own version of `get_id_card_info()`, and Python dynamically chooses the right one **at runtime**.

# So you’re using **both duck typing** and **polymorphism** at the same time here 💯

# ---

# ### 🎯 Summary:
# | Concept         | Present in your code? | Why? |
# |----------------|-----------------------|------|
# | Duck Typing     | ✅ Yes                | Function works as long as method exists—no type check |
# | Polymorphism    | ✅ Yes                | Same method behaves differently for each class |

# ---

# Wanna take it a step further? You could add error handling or check what happens if you pass an object that doesn’t have the method. Want to try that?