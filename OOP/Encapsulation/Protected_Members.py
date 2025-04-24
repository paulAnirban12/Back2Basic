# 🛡️ Protected Members in Python
# ------------------------------
# ✅ Concept:
# Attributes intended to be accessed within the class and its subclasses.
# Not strictly private, but signal that access should be limited.

# 🧩 Syntax:
#   Protected Attribute
#   --------------------------
#   self._attribute_name

# ✅ Notes:
# - A single underscore (_) is used before the attribute name.
# - Still accessible from outside, but treated as "internal use only".
# - Common in class hierarchies to share data with child classes.


# 🎯 Objective: Create Employee and Manager classes
# - Employee class:
#   - Public attribute: name
#   - Protected attribute: _salary
#   - Method to display employee info

# - Manager subclass:
#   - Accesses and displays _salary (protected)

# Demonstrates how _salary can be accessed inside the class but should not be accessed from outside.

class Employee:
    def __init__(self, Name, Id, Position):
        self.__salary = 0  # Private attribute, not directly accessible outside
        self.Name = Name
        self.Id = Id
        self.Position = Position

        # Set salary based on position
        if self.Position == "Manager":
            self.__salary = 70000
        elif self.Position == "Officer":
            self.__salary = 40000
        else:
            self.__salary = 30000

    @property
    def salary(self):
        return self.__salary  # Read-only salary property

    def _update_salary(self, amount):
        self.__salary += amount  # Internal method to safely update salary

    def employee_info(self):
        print(f"Id:{self.Id}")
        print(f"Name:{self.Name}")
        print(f"Position:{self.Position}")
        print(f"Salary:{self.__salary}")  # Displays salary (can't be changed directly)


class Manager(Employee):
    def __init__(self, Name, Id, Position):
        super().__init__(Name, Id, Position)

    def Update_Salary(self, obj, amount):
        # Print salary change message
        if amount < 0:
            print(f"{obj.Name}'s salary has been decreased by {-amount} as of today.")
        else:
            print(f"{obj.Name}'s salary has been increased by {amount} as of today.")

        obj._update_salary(amount)  # Update salary using the internal method


# Create an employee and show their info
Employee1 = Employee("AP", 1256, "Officer")
Employee1.employee_info()  # Shows original salary (not updated yet)

# Create a manager and update salary of Employee1
Manager1 = Manager("ANP", 125, "Manager")
Manager1.Update_Salary(Employee1, -2500)  # Decrease salary of Employee1
Employee1.employee_info()  # Shows updated salary

# Try to change salary directly (this will fail)
Employee1.__salary = 45000  # This will raise an error because __salary is private
Employee1.employee_info()  # Will still show original salary (not updated directly)


    


        


    