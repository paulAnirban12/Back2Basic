# # Instance Method vs Class Method vs Static Method
# | Instance Method               | Class Method                    | Static Method                   |
# |-------------------------------|----------------------------------|---------------------------------|
# | self                          | cls (using @classmethod)         | None (no self or cls)           |
# | Works with objects (instances) | Works with class itself         | Neither instance nor class      |
# | Must use self                  | Must use @classmethod decorator  | Must use @staticmethod decorator |
# | Example: def method(self):     | @classmethod def method(cls):    | @staticmethod def method():      |
# | Can modify instance data       | Can modify class data            | Cannot modify instance or class |



# Class: Library
# Attributes:
# - members: List of all library members (class-level)

# Methods:
# - join_member(): Adds a new member to the library (instance method)
# - calculate_late_fee(overdue_days): Calculates late fee for overdue books (static method)
# - get_all_members(): Returns all library members (class method)

class Library:
    members = []
    membership = 0
    def join_member(self,name,gender,contact):
      Library.membership += 1
      self.name = name
      self.gender = gender
      self.contact = contact
      self.membership = Library.membership
      Library.members.append(self)
         

    @staticmethod
    def calculate_late_fee(obj,overdue_days):
        name = obj.name
        if overdue_days == 0:
           print(f"{name} is on time. So no late fee!")
        else:
            if overdue_days < 30:
                print(f"{name} is {overdue_days} days late. So The late fee is {50*overdue_days}")
            elif overdue_days == 30:
                print(f"{name} is a month late. So The late fee is {50*overdue_days}")
            else:
                if overdue_days < 365:
                    month = overdue_days//30
                    days = overdue_days%30
                    if days == 0:
                        print(f"{name} is {month} months late. So The late fee is {50*overdue_days}")
                    else:
                        print(f"{name} is {month} months and {days} days late. So The late fee is {50*overdue_days}")
                elif overdue_days == 365:
                    print(f"{name} is 1 year late. So The late fee is {50*overdue_days}")
                else:
                    if obj.gender == "M":
                        print(f"{name} is more than a year late. So he is sued for fraud.")
                    else:
                        print(f"{name} is more than a year late. So she is sued for fraud.")
            
                   

                

    @staticmethod
    def get_info(human):
       print(f"Membership No:{human.membership}")
       print(f"Name:{human.name}")
       print(f"Contact:{human.contact}")
       
       

    @classmethod
    def get_all_members(cls):
       for member in cls.members:
          Library.get_info(member)      

member1 = Library()
member1.join_member("A","M",+8801589784532)


member2 = Library()
member2.join_member("ABC","F",+8801589284532)


member3 = Library()
member3.join_member("X","M",+8801599784532)

member4 = Library()
member4.join_member("Y","F",+8801589744532)

Library.get_all_members()

Library.calculate_late_fee(member1, 50)
Library.calculate_late_fee(member2, 00)
Library.calculate_late_fee(member3, 150)
Library.calculate_late_fee(member4, 450)


