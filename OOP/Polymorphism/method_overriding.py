"""
Imagine your mom makes cookies 🍪 one way.
But you want to make them your own special way!
So you use the same recipe name, but change what’s inside.

That’s called method overriding —
You take something from your parents (the base class)
and change it your way in your version (the child class)!
"""

class Mom:

    def make_cookies(self):
        print("Mom's Recipe")

class Child(Mom):
    
    def make_cookies(self):
        print("Child's Recipe") 


child = Child()
child.make_cookies()

# 🛍️ Scenario: You’re building an Online Shopping System
# You have a base class called User, and two types of users:
# 1.Customer
# 2.Admin
# Each user has a method access_portal()
# But customers and admins use the same method name to do different things — that’s method overriding!

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password =password
    def access_portal(self):
        print(f"Name:{self.name}")
        print(f"Email:{self.email}")
        print(f"Password:{self.password}")

class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def access_portal(self):
        print(f"I am admin, my credentials should not be revealed")

class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def access_portal(self):
        print(f"Name:{self.name}")
        print(f"Email:{self.email}")
        print("Do you want to change anything here??")        


admin1 = Admin("X","fgh@gmail.com","45678")
admin1.access_portal()

customer1 = Customer("X","fgh@gmail.com","45678")
customer1.access_portal()
