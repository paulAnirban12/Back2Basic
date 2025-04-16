class Calculator:

    def add(self, *numbers):
        result = 0
        for i in numbers:
            result += i
        return result

    def subtract(self, *numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
        

    def multiply(self, *numbers):
        result = 1
        for num in numbers:
            result *= num
        return result
        print(f"The multiplication is {result:.2f}")

    def divide(self, *numbers):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            return result
            print(f"The division is {result:.2f}")
        except ZeroDivisionError:
            print("Error: Division by zero")

    def remainder(self, *numbers):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result %= num
            return result
            print(f"The remainder is {result:.2f}")
        except ZeroDivisionError:
            print("Error: Division by zero")

    


class ScientificCalculator(Calculator):

    def average(self, *numbers):
        result = self.add(*numbers)
        total_numbers = len(numbers)
        result /= total_numbers
        print(f"The average of {numbers} is {result:.2f}")

    def MaxMin(self, *numbers):
        maximum = numbers[0]
        minimum = numbers[0]
        for num in numbers:
            if maximum < num:
                maximum = num
            if minimum > num:
                minimum = num
        print(f"The maximum value of {numbers} is {maximum}")
        print(f"The minimum value of {numbers} is {minimum}")

    def degrees_to_radians(self, degrees):
        return degrees * (3.141592653589793 / 180)

    def factorial(self, number):
        result = 1
        for i in range(number, 0, -1):
            result *= i
        return result

    def sin(self, degree):
        radian = self.degrees_to_radians(degree)
        result = 0
        for i in range(5):
            sign = (-1) ** i
            term = (radian ** (2 * i + 1)) / self.factorial(2 * i + 1)
            result += sign * term
        print(f"Sin({degree}) = {result:.2f}")

    def cos(self, degree):
        radian = self.degrees_to_radians(degree)
        result = 0
        for i in range(5):
            sign = (-1) ** i
            term = (radian ** (2 * i)) / self.factorial(2 * i)
            result += sign * term
        print(f"Cos({degree}) = {result:.2f}")

    def power(self, base, power):
        result = 1
        for _ in range(power):
            result *= base
        print(f"The answer of {base}^{power} is {result:.2f}")

    def root(self, number, power):
        import cmath
        if number < 0:
            if power % 2 == 0:
                result = cmath.exp(cmath.log(number) / power)
                print(f"The {power}th root of {number} is a complex number: {result:.2f}")
            else:
                root = 1 / power
                result = -((-number) ** root)
                print(f"The {power}th root of {number} is {result:.2f}")
        else:
            root = 1 / power
            result = number ** root
            print(f"The {power}th root of {number} is {result:.2f}")

    

    


calc = ScientificCalculator()

while True:
    print("" + f"{'---- Calculator Menu ----':^60}")
    operations = [
    "1. Add", "2. Subtract", "3. Multiply",
    "4. Divide", "5. Remainder", "6. Power",
    "7. Root", "8. Factorial", "9. Average",
    "10. Max/Min", "11. Sin", "12. Cos"
]

    for i in range(0, len(operations), 3):
        print(f"{operations[i]:<20}{operations[i+1]:<20}{operations[i+2]:<20}")
    option = int(input("Select Option:"))
    if option in [1,2,3,4,5,9,10]:
        
        if option == 1:
            print(f"You have selected {option} for addition")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            print(f"The addition is {calc.add(*numbers):.2f}")
            
        elif option == 2:
            print(f"You have selected {option} for subtraction")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            print(f"The subtraction is {calc.subtract(*numbers):.2f}")
            
        elif option == 3:
            print(f"You have selected {option} for multiplication")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            print(f"The multiplication is {calc.multiply(*numbers):.2f}")
            
        elif option == 4:
            print(f"You have selected {option} for division")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            print(f"The division is {calc.divide(*numbers):.2f}")
            
        elif option == 5:
            print(f"You have selected {option} for remainder")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            print(f"The remainder is {calc.remainder(*numbers):.2f}")
            
        elif option == 9:
            print(f"You have selected {option} for average")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            calc.average(*numbers)
        else:
            print(f"You have selected {option} for MaxMin")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            calc.MaxMin(*numbers)

    elif option in [6,7,8]:
        if option == 6:
            print(f"You have selected {option} for Power")
            base = float(input("Base:"))
            power = int(input("Power:"))
            calc.power(base,power)
        elif option == 7:
            print(f"You have selected {option} for Root")
            base = float(input("Base:"))
            root = int(input("Root:"))
            calc.root(base,root)
        else:
            print(f"You have selected {option} for Factorial")
            value = int(input("Value for factorial:"))
            print(f"The factorial of {value}, {value}! = {calc.factorial(value)}")
            

    elif option in [11,12]:
        if option == 11:
            print(f"You have selected {option} for Sine")
            degree = int(input("Degree:"))
            calc.sin(degree)
        else:
            print(f"You have selected {option} for Cosine")
            degree = int(input("Degree:"))
            calc.cos(degree)
    else:
        break
        



