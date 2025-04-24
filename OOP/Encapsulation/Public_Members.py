# Public members: accessible anywhere (in/outside class or module), no special syntax needed

# 🎯 Scenario: Product Inventory Management
# Class Name: Product
# Attributes:
# - product_name (public): Name of the product
# - price (public): Price of the product
# - stock_quantity (public): Quantity of the product in stock

# Method Names:
# - update_stock(): Adds new items to stock
# - sell_product(): Decreases stock when sold
# - display_details(): Displays product info (name, price, stock)

# 📌 Public Members Usage:
class Product:
    product_id = 10000
    # ✅ product_id (Public Class Attribute)
    # ✅ product_name, price, stock_quantity (Public Attributes)
    def __init__(self,product_name,price,stock_quantity):# - Set in __init__ when creating a Product
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity
        Product.product_id +=1 # - Auto-incremented to generate unique product IDs
        self.product_id = Product.product_id # -product_id Shared among all Product instances
    # ✅ Public methods:

    def display_details(self):# Accesses public attributes to display data
        print(f"Product_Id:{self.product_id}")# -product_id Shared among all Product instances
        print(f"Product_name:{self.product_name}")
        print(f"Price:{self.price}")
        if self.stock_quantity == 0:
            print(f"Stocked Out!!!")
        elif self.stock_quantity <= 10:
            print(f"There are only {self.stock_quantity} pieces left.So Have to stock up.")
        else:
            print(f"Stock_quantity:{self.stock_quantity}")

    def update_stock(self,new_stock):# Modifies stock_quantity
        self.stock_quantity += new_stock
        print(f"Stock of {self.product_name} have increased as {new_stock} new units have been added to the stock today.")

    def sell_product(product,numbers):# Modifies stock_quantity using product object
        product.stock_quantity -= numbers
        print(f"Stock of {product.product_name} have decreased as {numbers} pieces of {product.product_name} have been sold today.")

    
product1 = Product("HP Laptop",50000,45)
# - Accessed & modified in:
product1.display_details() #   -  to show info
product1.update_stock(10)  #   -  to increase stock
product1.display_details() #   -  to show info
Product.sell_product(product1,10) # -  to decrease stock
product1.display_details() #   -  to show info










