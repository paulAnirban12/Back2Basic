## 🔁 Polymorphism in Python

This section covers:
1.Duck Typing:       Toys → All have draw() and make_toy_draw() calls it without caring about the type 
2.Method Overriding: Mom → Child (Child overrides make_cookies() method from Mom)  
3.Method Overloading: Same method name with different number of arguments (handled via default values). 
Student.add() method works with 1, 2, or 3 marks like **add(69), add(69,45), or add(69, 45, 96)  
4.Operator Overloading:Same operator behaves differently based on objects. 
  _e.g., **Student1 + Student2** → Adds marks from both students using **__add__() method
