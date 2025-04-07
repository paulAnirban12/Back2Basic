# Start with the Second Element – Assume the first element is already sorted.

# Compare with Previous Elements – Shift larger elements to the right.

# Insert the Current Element in the Correct Position.

# Repeat for All Elements until the entire list is sorted.
# Example
# Unsorted List:
# [5, 3, 8, 4, 2]

# Pass 1:
# Take 3 (2nd element).

# Compare with 5, shift 5 right.

# Insert 3 in its correct position.

# List after pass: [3, 5, 8, 4, 2]

# Pass 2:
# Take 8 (3rd element).

# No shifting needed, as 8 > 5.

# List remains: [3, 5, 8, 4, 2]

# Pass 3:
# Take 4 (4th element).

# Compare with 8 → shift 8 right.

# Compare with 5 → shift 5 right.

# Insert 4 in its correct position.

# List after pass: [3, 4, 5, 8, 2]

# Pass 4:
# Take 2 (5th element).

# Compare with 8, 5, 4, and 3 → shift them all right.

# Insert 2 at the beginning.

# List after pass: [2, 3, 4, 5, 8]

# ✅ Sorted List: [2, 3, 4, 5, 8]
# Time Complexity
# Best Case (Already Sorted): O(n)

# Worst & Average Case: O(n²)

# \

arr = list(map(int, input("Unsorted List: ").split(',')))
size = len(arr)

for i in range(size-1):
    j = i+1
    flag = 0
    print("Now we will check",arr[j])
    while j > 0:
        
        if arr[j-1] > arr[j]:
            print(f"{arr[j-1]} and {arr[j]} will swap places")
            arr[j-1],arr[j] = arr[j], arr[j-1]
            flag = 1
        
        j -= 1
    

    if flag == 1:

        print(f"Pass {i+1}:",arr)
    else:
        print("No swaps were made")