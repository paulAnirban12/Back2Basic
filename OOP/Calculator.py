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
        
    def factorial_degrees(numbers):
        if numbers == 0:
            return 1
        else:
            result = 1
            for i in range(numbers,0,-1):
                result *= i
            return result
            
        
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

    def degrees_to_radians(self,degrees):
        return degrees * (3.141592653589793 / 180)

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
print("Basic Functions")
calc.add(565,256,125,789)
calc.substract(545,789,-250)
calc.multiply(454,898,256)
calc.divide(454,2,0)
calc.remainder(45,12,0)
print("Advanced Functions")
calc.power(45,23)
calc.root(45,6)
calc.factorial(45)
print("New Functions")
calc.average(73,482,9,1056,8723)
calc.MaxMin(73,482,9,1056,8723)
print("Trigonometric Functions")
calc.sin(30)
calc.cos(60)

