# 🛒 Online Retail Store System — Demonstrating Polymorphism
#
# 📚 Classes and Attributes:
# ➔ Product: name, category, price
# ➔ Electronics: brand, model
# ➔ Clothes: size, color
# ➔ Groceries: expiry_date, category
#
# 🔥 Polymorphism Types:
#
# # 📌 apply_discount() — Method Overriding Logic
#
# Class          | Discount Logic
# -------------- | --------------------------------------------------
# Electronics    | 10% off if price > $100
# Clothes        | $20 off if price > $50
# Groceries      | Special discount if seasonal deal available
#
# 🎯 Each class customizes apply_discount() differently!

# 📌 calculate_price() — Method Overloading Logic
#
# Class          | Price Calculation Logic
# -------------- | ----------------------------------------------------
# Product        | Returns base price
# Electronics    | 10% off if price > $100, else return base price
# Clothes        | $20 off if price > $50, else return base price
# Groceries      | Discount if expiry is near, else return base price
#
# 🎯 Each class customizes calculate_price() differently!
#
# 📌 Duck Typing (Dynamic):
#    - recommend_product() behaves differently but called the same way:
#        • Electronics ➔ Suggest accessories
#        • Clothes ➔ Suggest seasonal trends
#        • Groceries ➔ Suggest fresh produce deals

from dataclasses import dataclass, field
import random
from datetime import datetime, date

# Base class representing a generic Product
@dataclass
class Product:
    name: str
    category: str
    price: float
    id: int = field(default_factory=lambda: random.randint(10000, 99999), init=False)

    # Post-initialization method to print product details
    def __post_init__(self):
        print(f"{self.name} has been added to the database with the id {self.id}")

    # Method for calculating price with overloading: 
    # 1 argument (quantity), or 2 arguments (quantity + discount)
    def calculate_price(self, *args):
        if len(args) == 1:
            # Calculate price based only on quantity
            quantity = args[0]
            return self.price * quantity
        elif len(args) == 2:
            # Calculate price with both quantity and discount
            quantity, discount = args
            return self.price * quantity - discount
        else:
            raise ValueError("Invalid number of arguments")

    # Method to apply discount (for the base class, this is a simple print statement)
    def apply_discount(self, discount):
        print(f"Price after discount: {self.price - discount}")
    
    # Method to recommend related products (generic method)
    def recommend_product(self):
        print(f"It seems that you searched for {self.name}. If you like, you can also check out the other items from {self.category}!")

# Electronics subclass that overrides the base class methods for electronics-specific logic
@dataclass
class Electronics(Product):
    brand: str
    model: str

    # Post-initialization to add specific details for electronics products
    def __post_init__(self):
        super().__post_init__()
        print(f"Product: {self.name}\nBrand: {self.brand}")

    # Overridden calculate_price with model-specific discounts for electronics
    def calculate_price(self, quantity=1):
        if self.category in ["Smartphone", "smartphone"]:
            # Logic for smartphone pricing based on model
            if self.brand == "Apple":
                if self.model == "iphone 13":
                    price = self.price * quantity * 0.8
                    discount = 20
                elif self.model == "iphone 14":
                    price = self.price * quantity * 0.85
                    discount = 15
                elif self.model == "iphone 15":
                    price = self.price * quantity * 0.9
                    discount = 10
                elif self.model == "iphone 16":
                    price = self.price * quantity * 0.95
                    discount = 5
                else:
                    price = self.price * quantity * 0.7
                    discount = 30
            elif self.brand == "Samsung":
                price = self.price * quantity * 0.8
                discount = 20
            else:
                price = self.price * quantity * 0.7
                discount = 30
        elif self.category in ["Laptop", "laptop"]:
            # Logic for laptop pricing based on brand
            if self.brand == "Apple":
                price = self.price * quantity * 0.9
                discount = 10
            elif self.brand in ["HP", "Dell", "Asus"]:
                price = self.price * quantity * 0.85
                discount = 15
            else:
                price = self.price * quantity * 0.8
                discount = 20
        else:
            # Default pricing logic
            if self.price * quantity > 150000:
                price = self.price * quantity - 12000
                discount = int((12000 * 100) / (self.price * quantity))

        return price, discount

    # Method to apply discount and print relevant information for electronics
    def apply_discount(self):
        quantity = int(input(f"Enter the amount of {self.name} you want to buy: "))
        price, discount = self.calculate_price(quantity)
        if price is None:
            print(f"The model {self.name} is not available now.")
        else:
            print(f"Original Price of {self.name} for {quantity} units: {self.price * quantity}.")
            print(f"Price after {discount}% discount: {price}.")
            print(f"Therefore, you save {self.price * quantity - price}")

    # Recommends related products based on the electronics category
    def recommend_product(self):
        super().recommend_product()

# Clothes subclass with its own pricing and discount logic
@dataclass
class Clothes(Product):
    size: str
    color: str

    # Post-initialization to determine the category and print details
    def __post_init__(self):
        super().__post_init__()
        # Adjusting the category and size
        if self.size == "S":
            size = "Small"
        elif self.size == "M":
            size = "Medium"
        elif self.size == "L":
            size = "Large"
        elif self.size == "XL":
            size = "Extra Large"
        else:
            size = "Unknown"
        print(f"Product: {self.name} ({self.category} {self.color})\nSize: {size}")

    # Overloaded calculate_price method with size-specific discounts
    def calculate_price(self, quantity):
        price = super().calculate_price(quantity)
        if price > 5000:
            price -= 500
        return price

    # Method to apply discount for clothes items
    def apply_discount(self):
        quantity = int(input(f"Enter the number of {self.name} you want: "))
        price = self.calculate_price(quantity)
        print(f"Total price for {quantity} {self.name}: {self.price * quantity}")
        print(f"After discount, you pay: {price}")

    # Recommends related products in the same category
    def recommend_product(self):
        print(f"It seems that you searched for {self.name}. If you like, you can also check out other items from {self.category}!")

# Groceries subclass with expiry-based pricing logic
@dataclass
class Groceries(Product):
    expiry_date: date

    # Post-initialization to print expiry details and handle product restrictions
    def __post_init__(self):
        super().__post_init__()
        if self.category.lower() in ["vegetable", "veggies"]:
            print("Not acceptable")
            exit()
        else:
            print(f"Product: {self.name}\nCategory: {self.category}\nExpiry Date: {self.expiry_date.strftime('%B %d, %Y')}")

    # Method to calculate price, applying logic based on expiry dates
    def calculate_price(self, quantity=1):
        return super().calculate_price(quantity)

    # Apply discount based on expiry date (e.g., discount for soon-to-expire items)
    def apply_discount(self):
        today = date.today()
        timeline = self.expiry_date - today
        price = self.calculate_price()
        if timeline.days >= 365:
            print(f"You have to pay {price} for {self.name}.")
        elif timeline.days <= 270:
            print(f"You have to pay {price * 0.8} for {self.name}.")
        elif timeline.days <= 180:
            print(f"You have to pay {price * 0.6} for {self.name}.")
        elif timeline.days <= 90:
            print(f"You have to pay {price * 0.5} for {self.name}.")
        elif timeline.days <= 30:
            print("This item is about to expire soon. We recommend a fresh piece instead.")

    # Recommends related products from the same category
    def recommend_product(self):
        super().recommend_product()

# Test case for Electronics product
electronic_product = Electronics("Samsung Galaxy A50", "Smartphone", 45000, "Samsung", "Galaxy A")
electronic_product.apply_discount()
electronic_product.recommend_product()

# Test case for Clothes product
clothing_item = Clothes("Shirt", "Gents Collection", 425, "M", "Black")
clothing_item.apply_discount()
clothing_item.recommend_product()

# Test case for Groceries product
expiry_date = datetime.strptime(input("Enter expiry date (DD-MM-YYYY): "), "%d.%m.%Y").date()
grocery = Groceries("Pepsi", "Beverage", 150, expiry_date)
grocery.apply_discount()
grocery.recommend_product()

