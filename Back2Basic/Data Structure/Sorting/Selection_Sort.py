# 1.Find the Minimum Element – Search the entire list for the smallest element.

# 2.Swap It with the First Unsorted Element – Place it at the beginning of the unsorted section.

# 3.Repeat for the Remaining Elements – Continue this process, ignoring the already sorted section.
# Example
# Unsorted List:
# [5, 3, 8, 4, 2]

# Pass 1:
# Find the smallest element → 2

# Swap 2 with the first element (5)

# List after swap: [2, 3, 8, 4, 5]

# Pass 2:
# Find the smallest in remaining → 3

# Swap 3 with itself (no change)

# List remains: [2, 3, 8, 4, 5]

# Pass 3:
# Find the smallest in remaining → 4

# Swap 4 with 8

# List after swap: [2, 3, 4, 8, 5]

# Pass 4:
# Find the smallest in remaining → 5

# Swap 5 with 8

# List after swap: [2, 3, 4, 5, 8]

# ✅ Sorted List: [2, 3, 4, 5, 8]
# Best, Worst & Average Case: O(n²)

arr = list(map(int, input("Unsorted list: ").split(',')))
size = len(arr)

for i in range(size):
    min_index = i  # Store index of the minimum element

    for j in range(i + 1, size):
        if arr[j] < arr[min_index]:
            min_index = j  # Update index of minimum element

    if min_index != i:
        print(arr[i], "and", arr[min_index], "will swap places.")
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap correctly

    else:
        if i < size - 1:  # Avoid printing for the last element
            print("No swaps were made.")    

    if i < size - 1:
        print("The array is now:", arr)
print("Sorted list:", arr)

