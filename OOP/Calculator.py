class Calculator:

    
    def add(self,*numbers):
        result  = 0
        for i in numbers[0:]:
            result += i
        print(f"The addition is {result}")

    def substract(self,*numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        
        print(f"The substraction is {result}")

    def multiply(self,*numbers):
        result = 1
        for num in numbers[0:]:
            result *= num
        print(f"The multiplication is {result}")

    def divide(self,*numbers):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            print(f"The division is {result:.2f}")
        except ZeroDivisionError:
            print("Error: Division by zero")
    
    def remainder(self,*numbers):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result %= num
            print(f"The remainder is {result}")
        except ZeroDivisionError:
            print("Error: Division by zero")
    
    def power(self,base,power):
        result = 1
        if power == 0:
            pass
        else:
            result = 1
            for i in range(1,power+1):
                result *= base

        print(f"The answer of {base}^{power} is {result}")
    
    
    def root(self,numbers,power):
        import cmath
        if numbers < 0:
            if power % 2 == 0:
                # Even root of negative number → complex result
                result = cmath.exp(cmath.log(numbers) / power)
                if power == 2:
                    print(f"As {numbers} is negative, the square root of {numbers} is a complex number which is {result}")
                else:
                    print(f"Since {numbers} is negative, the {power}th root is a complex number: {result}")
            else:
            # Odd root of negative → real number
                root = 1 / power
                result = -((-numbers) ** (root))
                if power == 3:
                    print(f"The cube root of {numbers} is {result:.2f}")
                else:
                    print(f"The {power}th root of {numbers} is {result:.2f}")
        else:
        # Positive number → normal calculation
            root = 1 / power
            result = numbers ** root
            if power == 2:
                print(f"The square root of {numbers} is {result:.2f}")
            elif power == 3:
                print(f"The cube root of {numbers} is {result:.2f}")
            else:
                print(f"The {power}th root of {numbers} is {result:.2f}")

    

    def factorial(self,numbers):
        if numbers == 0:
            return 1
        else:
            result = 1
            for i in range(numbers,0,-1):
                result *= i
            print(f"The factorial of {numbers}, {numbers}! = {result}")
        
    
        
    def average(self,*numbers):
        result = 0
        count = 0
        for num in numbers[0:]:
            count += 1
            result += num
        result /= count
        print(f"The average of {numbers} is {result:.2f}")

    
    def MaxMin(self,*numbers):
        Max = numbers[0]
        Min = numbers[0]
        for i in numbers[1:]:
            if Max < i:
                Max = i
            if Min > i:
                Min = i
        print(f"The maximum value of {numbers} is {Max}")
        print(f"The miniimum value of {numbers} is {Min}")

    class Trigonometric_Calculator:
        @staticmethod
        def degrees_to_radians(degrees):
            return degrees * (3.141592653589793 / 180)
        @staticmethod
        def factorial_degrees(numbers):
            if numbers == 0:
                return 1
            else:
                result = 1
                for i in range(numbers,0,-1):
                    result *= i
                return result
        def sin(self,degree):
            deg = Calculator()
            radian = deg.degrees_to_radians(degree)
            result = 0
            for i in range(5):
                sign = (-1) ** i
                term = (radian ** (2*i + 1)) / Calculator.factorial_degrees(2*i + 1)
                result += sign * term
            print(f"Sin({degree}) = {result:.2f}")

        def cos(self,degree):
            deg = Calculator()
            radian = deg.degrees_to_radians(degree)
            result = 0
            for i in range(5):
                sign = (-1) ** i
                term = (radian ** (2*i)) / Calculator.factorial_degrees(2*i)
                result += sign * term
            print(f"Cos({degree}) = {result:.2f}")



calc = Calculator()
trig = Calculator.Trigonometric_Calculator()
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
            calc.add(*numbers)
        elif option == 2:
            print(f"You have selected {option} for substraction")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            calc.substract(*numbers)
        elif option == 3:
            print(f"You have selected {option} for multiplication")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            calc.multiply(*numbers)
        elif option == 4:
            print(f"You have selected {option} for division")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            calc.divide(*numbers)
        elif option == 5:
            print(f"You have selected {option} for remainder")
            numbers = list(map(float,input("Enter numbers:").split(',')))
            calc.remainder(*numbers)
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
            calc.factorial(value)

    elif option in [11,12]:
        if option == 11:
            print(f"You have selected {option} for Sine")
            degree = int(input("Degree:"))
            trig.sin(degree)
        else:
            print(f"You have selected {option} for Cosine")
            degree = int(input("Degree:"))
            trig.cos(degree)
    else:
        break
        



