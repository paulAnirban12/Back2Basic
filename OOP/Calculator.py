class Calculator:

    
    def add(*numbers):
        result = sum(numbers)
        print(f"The addition is {result}")

    def substract(*numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        
        print(f"The substraction is {result}")

    def multiply(*numbers):
        result = 1
        for num in numbers[0:]:
            result *= num
        print(f"The multiplication is {result}")

    def divide(*numbers):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            print(f"The division is {result:.2f}")
        except ZeroDivisionError:
            print("Error: Division by zero")
    
    def remainder(*numbers):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result %= num
            print(f"The remainder is {result}")
        except ZeroDivisionError:
            print("Error: Division by zero")
    # mod,power,sqrt,factorial,avg,max,min,sin,cos,tan
    def power(base,power):
        result = 1
        if power == 0:
            pass
        else:
            result = 1
            for i in range(1,power+1):
                result *= base

        print(f"The answer of {base}^{power} is {result}")
    
    
    def root(numbers,power):
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

    

    def factorial(numbers):
        if numbers == 0:
            return 1
        else:
            result = 1
            for i in range(numbers,0,-1):
                result *= i

            return result
            
        
    def average(*numbers):
        result = 0
        count = 0
        for num in numbers[0:]:
            count += 1
            result += num
        result /= count
        print(f"The average of {numbers} is {result:.2f}")

    def MaxMin(*numbers):
        Max = numbers[0]
        Min = numbers[0]
        for i in numbers[1:]:
            if Max < i:
                Max = i
            if Min > i:
                Min = i
        print(f"The maximum value of {numbers} is {Max}")
        print(f"The miniimum value of {numbers} is {Min}")

    def degrees_to_radians(degrees):
        return degrees * (3.141592653589793 / 180)

    def sin(degree):
        radian = Calculator.degrees_to_radians(numbers)
        result = 0
        for i in range(5):
            sign = (-1) ** i
            term = (radian ** (2*i + 1)) / Calculator.factorial(2*i + 1)
            result += sign * term
        print(f"Sin({degree}) = {result:.2f}")

    def cos(degree):
        radian = Calculator.degrees_to_radians(numbers)
        result = 0
        for i in range(5):
            sign = (-1) ** i
            term = (radian ** (2*i)) / Calculator.factorial(2*i)
            result += sign * term
        print(f"Cos({numbers}) = {result:.2f}")


numbers = list(map(int, input("Enter numbers for addition: ").split()))
Calculator.add(*numbers)
Calculator.substract(*numbers)
Calculator.multiply(*numbers)
Calculator.divide(*numbers)
Calculator.remainder(*numbers)
Calculator.average(*numbers)
Calculator.MaxMin(*numbers)

base = int(input("Enter number:"))
power = int(input("Enter root:"))
Calculator.power(base,power)
Calculator.root(base,power)

numbers = int(input("Enter number: "))
result =  Calculator.factorial(numbers)
print(f"The factorial of {numbers} is, {numbers}! = {result}")

numbers = int(input("Enter degree: "))
Calculator.sin(numbers)
Calculator.cos(numbers)


