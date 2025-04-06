def fibonacci(x):
    
    
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)




value = int(input("Enter Value: "))
fibonacci_series = []
for i in range(1,value+1):

    fibonacci_series.append(fibonacci(i))

print(fibonacci_series)