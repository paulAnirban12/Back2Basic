arr = list(map(int, input("Numbers: ").split(',')))
size = len(arr)
index = int(input("Index_Number:"))

for i in range(size):
    if i == index:
        print(f"{arr[i]} is the {index}th number of the list.")
        break