# Abstract Method: The method which is only declared, but not defined
# Abstract Class:The class which has abstract method.
# For abstract class and method you have to use "from abc import ABC, abstractmethod"

# Vehicle is an abstract class — it says "move()" must exist,
# but doesn’t say how. Car is a real class that shows how it moves.


from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):

    def move(self):
        print("Accelerator+Brake+Clutch")
# v1 = Vehicle()
# v1.move()

v2 = Car()
v2.move()

# Vehicle is an abstract class — move() is just a rule here.
# Car inherits Vehicle and gives a real meaning to move().
# Abstract class can't be used directly (like Vehicle()).


# ✈️ Airline System Example:
# Employee is an abstract class with a perform_duty() method.
# Pilot, Flight Attendant, and Ground Staff each define it differently.
# 👨‍✈️ Pilot – flies the plane
# 🧑‍✈️ Flight Attendant – handles passenger safety
# 🧑‍🔧 Ground Staff – manages baggage and runway prep
# Abstract method = rule all roles must follow, but with their own logic.

from abc import ABC, abstractmethod
class Employee(ABC):
        @abstractmethod
        def perform_duty(self):
             pass
class Pilot(Employee):
        def perform_duty(self):
            print("Flies the plane")
class FlightAttendant(Employee):
        def perform_duty(self):
            print("Handles passenger safety")
class GroundStaff(Employee):
        def perform_duty(self):
            print("Manages baggage and runway prep")

Employee1 = Pilot()
Employee1.perform_duty()
Employee2 = FlightAttendant()
Employee2.perform_duty()
Employee3 = GroundStaff()
Employee3.perform_duty()
            
               
