
# Same method add(),
# but it works with no numbers, one number, or two numbers.
# That’s method overloading — one method, many forms!

class Student:

    def __init__(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def add(self,a = None,b = None,c = None):
        if a != None and b != None and c != None:
            return a+b+c
        elif a != None and b != None:
            return a+b
        elif a != None:
            return a
        else:
            return 0
    
s1 = Student(69,45)
print(s1.add(69,45,96))

# 🎯 Scenario: You're building an E-Commerce Invoice System
# You want the same method to generate invoices, but with:
# 1.Only product name
# 2.Product name + quantity
# 3.Product name + quantity + discount

class Product:

    def __init__(self,price):
        self.price = price

    def invoice(self,name = None,quantity = None,discount = None):

        if name != None and quantity != None and discount != None:
            print(f"Product Name:{name}")
            print(f"Product Quantity:{quantity}")
            
            total = quantity * self.price
            print(f"Total price = {quantity} x ${self.price} = ${total}")
            print(f"Discount:{discount}")
            decimal = discount/100
            total = total - total * decimal
            print(f"Product Price after {discount}% discount:${total}")
        elif name != None and quantity != None:
            print(f"Product Name:{name}")
            print(f"Product Quantity:{quantity}")
            total = quantity * 500
            print(f"No discount. So Total price = {quantity} x ${self.price} = ${total}")

        elif name != None:
            print(f"Product Name:{name}")
            print(f"Total price = ${self.price}")
        else:
            print("No product was selected.")

product = Product(100)

product.invoice("Dove")
product.invoice("Nike",6)
product.invoice("HP",9,36)
product.invoice()
