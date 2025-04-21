
## 🔁 Polymorphism in Python

This section covers:
- **Duck Typing**:  
  Same method name in unrelated classes.  
  _e.g., , ,  → all have  and  calls it without caring about the type._

-- **Method Overriding**:  
  Child class changes behavior of a parent method.  
  _e.g.,  (Child overrides  from Mom)_


- **Method Overloading** (Not native):  
  Same method name, different args (use , default values).  
  _e.g.,  vs _

- **Operator Overloading**:  
  Redefine operators for custom objects.  
  _e.g.,  adds coordinates_


Check the files inside the  folder for examples.

## 🔁 Polymorphism in Python

This section covers:
- **Duck Typing**:
  Same method name in unrelated classes.
  _e.g., "Robot", "Dinosaur", "Fairy" → all have ".draw()" and "make_toy_draw()" calls it without caring about the type._

-- **Method Overriding**:
  Child class changes behavior of a parent method.
  _e.g., "Mom → Child" (Child overrides "make_cookies()" from Mom)_


- **Method Overloading** (Not native):
  Same method name, different args (use "*args", default values).
  _e.g., "add(2, 3)" vs "add(2, 3, 4)"_

- **Operator Overloading**:
  Redefine operators for custom objects.
  _e.g., "Point + Point" adds coordinates_
Check the files inside the  folder for examples.

## 🔁 Polymorphism in Python

This section covers:
- **Duck Typing**:
  Same method name in unrelated classes.
  _e.g., "Robot", "Dinosaur", "Fairy" → all have ".draw()" and "make_toy_draw()" calls it without caring about the type._

-- **Method Overriding**:
  Child class changes behavior of a parent method.
  _e.g., "Mom → Child" (Child overrides "make_cookies()" from Mom)_


- **Method Overloading** (Not native):
  Same method name, different args (use "*args", default values).
  _e.g., "add(2, 3)" vs "add(2, 3, 4)"_

- **Operator Overloading**:
  Redefine operators for custom objects.
  _e.g., "Point + Point" adds coordinates_
Check the files inside the  folder for examples.

## 🔁 Polymorphism in Python

This section covers:
- **Duck Typing**:  
  Same method name in unrelated classes.  
  _e.g., , ,  → all have  and  calls it without caring about the type._

-- **Method Overriding**:  
  Child class changes behavior of a parent method.  
  _e.g.,  (Child overrides  from Mom)_


- **Method Overloading** (Not native):  
  Same method name, different args (use , default values).  
  _e.g.,  vs _

- **Operator Overloading**:  
  Redefine operators for custom objects.  
  _e.g.,  adds coordinates_


Check the files inside the  folder for examples.

## 🔁 Polymorphism in Python

This section covers:
- **Duck Typing**:
  Same method name in unrelated classes.
  _e.g., "Robot", "Dinosaur", "Fairy" → all have ".draw()" and "make_toy_draw()" calls it without caring about the type._

-- **Method Overriding**:
  Child class changes behavior of a parent method.
  _e.g., "Mom → Child" (Child overrides "make_cookies()" from Mom)_


- **Method Overloading** (Not native):
  Same method name, different args (use "*args", default values).
  _e.g., "add(2, 3)" vs "add(2, 3, 4)"_

- **Operator Overloading**:
  Redefine operators for custom objects.
  _e.g., "Point + Point" adds coordinates_
Check the files inside the  folder for examples.

## 🔁 Polymorphism in Python

This section covers:

- **Duck Typing**  
  Use the same method name in unrelated classes.  
  _Example:_  
  Classes like **Robot**, **Dinosaur**, and **Fairy** all have a  method.  
  A function like  can call  on any of them — it doesn't care what type they are, just that they can draw!

- **Method Overriding**  
  A child class changes the behavior of a method it inherits from the parent class.  
  _Example:_  
  Class **Child** overrides  from class **Mom**, creating its own version of the same method.

- **Method Overloading** (Not natively supported in Python)  
  Use the same method name with different arguments using  or default parameters.  
  _Example:_  
   vs  — both use the same method, but handle different numbers of inputs.

- **Operator Overloading**  
  Redefine how operators like , , or  behave for your custom objects.  
  _Example:_  
   adds their coordinates, or  compares balances.

Check the files inside the "OOP/polymorphism/" folder for examples.
## Polymorphism in Python

This section covers:

- **Duck Typing**  
  Use the same method name in unrelated classes.  
  _Example:_  
  Classes like **Robot**, **Dinosaur**, and **Fairy** all have a  method.  
  A function like  can call  on any of them — it doesn't care what type they are, just that they can draw!

- **Method Overriding**  
  A child class changes the behavior of a method it inherits from the parent class.  
  _Example:_  
  Class **Child** overrides  from class **Mom**, creating its own version of the same method.

- **Method Overloading** (Not natively supported in Python)  
  Use the same method name with different arguments using  or default parameters.  
  _Example:_  
   vs  — both use the same method, but handle different numbers of inputs.

- **Operator Overloading**  
  Redefine how operators like , , or  behave for your custom objects.  
  _Example:_  
   adds their coordinates, or  compares balances.

## 🔁 Polymorphism in Python

This section covers:
**Duck Typing**:       Toys → All have **draw** method and **make_toy_draw** method calls it without caring about the type 
**Method Overriding**: Mom → Child (Child overrides **make_cookies** method from Mom)  
**Method Overloading**: Same method name with different number of arguments (handled via default values). 
**Student.add** method works with 1, 2, or 3 marks like **add 69**, **add 69, 45**, or **add 69, 45, 96 **_  
**Operator Overloading**:Same operator behaves differently based on objects. 
  _e.g., **Student1 + Student2** → Adds marks from both students using **__add__** method

Check the files inside the **OOP/polymorphism/** folder for examples.
