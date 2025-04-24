Python Object-Oriented Programming (OOP) Concepts - Demonstration

This repository demonstrates various core concepts of Object-Oriented Programming (OOP) in Python, including **Public**, **Protected**, and **Private** members, along with **Getters and Setters**. The examples cover different real-world scenarios such as Product Inventory Management, Employee and Manager systems, Bank Account handling, and Student Record Management.

## Contents
1. **Public Members**  
2. **Protected Members**  
3. **Private Members**  
4. **Getters and Setters**  

---

## 1. Public Members

Public members (attributes and methods) are accessible anywhere, both inside and outside the class.

### Scenario: Product Inventory Management
In this scenario, the **Product** class manages an inventory of products. Each product has a **public name**, **price**, and **stock quantity**. The system allows:
- Displaying product details such as name, price, and stock.
- Updating stock quantity when new stock is added.
- Decreasing stock when products are sold.

These public attributes and methods are directly accessible and can be modified freely from outside the class.

---

## 2. Protected Members

Protected members (attributes and methods) are intended to be accessed within the class and its subclasses, but not from outside the class directly. They are indicated by a single underscore (**_**).

### Scenario: Employee and Manager System
In this scenario, the **Employee** class stores employee details such as **name**, **id**, and **position**. The **salary** attribute is protected, meaning it can only be accessed or modified within the class and by subclasses (such as **Manager**). The system:
- Allows the Manager to access and modify employee salaries.
- Ensures that salary information is protected from direct modification from outside the class.

---

## 3. Private Members

Private members are not directly accessible from outside the class. They are indicated by a double underscore (**__**).

### Scenario: Bank Account System
In this scenario, the **BankAccount** class stores sensitive financial information such as **account number**, **account holder**, and **balance**. These private attributes are hidden from direct access:
- The **account_number**, **account_holder**, and **balance** are private and can only be manipulated using public methods such as **deposit()** and **withdraw()**.
- A method is provided to check and modify the account balance, ensuring no direct access from outside the class.

---

## 4. Getters and Setters

Getters and Setters are used to safely access and modify private attributes, following the principles of encapsulation. They provide controlled access to private data.

### Scenario: Book Management System
In this scenario, the **Book** class has private attributes such as **title** and **author**. The class includes:
- Getter methods to retrieve the book's title and author.
- Setter methods to modify the book's title and author.
This approach allows controlled access to these private attributes and prevents unauthorized modifications from outside the class.




