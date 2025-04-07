def factorial(x):

    if x == 0 or x == 1:
        return 1
    # elif x > 73:
    #     return "404 Error"
    else:
        return x * factorial(x-1)
    
value = int(input("Enter Number:"))
print(f"Factorial({value}) = {factorial(value)}")