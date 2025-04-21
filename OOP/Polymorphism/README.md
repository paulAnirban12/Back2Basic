## 🔁 Polymorphism in Python

This section covers:

- **Duck Typing**  
  Use the same method name in unrelated classes.  
  _Example:_  
  Classes like **Robot**, **Dinosaur**, and **Fairy** all have a `.draw()` method.  
  A function like `make_toy_draw()` can call `.draw()` on any of them — it doesn't care what type they are, just that they can draw!

- **Method Overriding**  
  A child class changes the behavior of a method it inherits from the parent class.  
  _Example:_  
  Class **Child** overrides `make_cookies()` from class **Mom**, creating its own version of the same method.

- **Method Overloading** (Not natively supported in Python)  
  Use the same method name with different arguments using `*args` or default parameters.  
  _Example:_  
  `add(2, 3)` vs `add(2, 3, 4)` — both use the same method, but handle different numbers of inputs.

- **Operator Overloading**  
  Redefine how operators like `+`, `-`, or `>` behave for your custom objects.  
  _Example:_  
  `Point + Point` adds their coordinates, or `Account1 > Account2` compares balances.
  
