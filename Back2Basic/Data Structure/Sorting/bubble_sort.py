# 1.Start at the Beginning – Compare the first two elements.

# 2.Swap if Necessary – If the first element is greater than the second, swap them.

# 3.Move to the Next Pair – Continue comparing and swapping adjacent elements until the largest element reaches the end (like a bubble floating up).

# 4.Repeat for Remaining Elements – Ignore the last sorted element and repeat the process until all elements are sorted.
# Example
# Unsorted List:
# [5, 3, 8, 4, 2]

# Pass 1:
# Compare 5 & 3 → Swap → [3, 5, 8, 4, 2]

# Compare 5 & 8 → No Swap → [3, 5, 8, 4, 2]

# Compare 8 & 4 → Swap → [3, 5, 4, 8, 2]

# Compare 8 & 2 → Swap → [3, 5, 4, 2, 8]
# (Largest element 8 is now at the end)

# Pass 2:
# Compare 3 & 5 → No Swap → [3, 5, 4, 2, 8]

# Compare 5 & 4 → Swap → [3, 4, 5, 2, 8]

# Compare 5 & 2 → Swap → [3, 4, 2, 5, 8]
# (Second largest element 5 is now in place)

# Pass 3:
# Compare 3 & 4 → No Swap → [3, 4, 2, 5, 8]

# Compare 4 & 2 → Swap → [3, 2, 4, 5, 8]

# Pass 4:
# Compare 3 & 2 → Swap → [2, 3, 4, 5, 8]

# ✅ Sorted List: [2, 3, 4, 5, 8]
# Best Case = O(n)
# Worst/Average Case = O(n²)

# for array as comma-separated numbers

arr = list(map(int, input("Enter numbers separated by commas: ").split(',')))
size = len(arr)
print("Unsorted list:", arr)

ascending = int(input("Sort in ascending order? (1 for Yes, 0 for No): "))

for i in range(size - 1):
    swapped = False  # To check if any swap happened

    for j in range(size - 1 - i):
        if (ascending == 1 and arr[j] > arr[j + 1]) or (ascending == 0 and arr[j] < arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap adjacent elements
            swapped = True
            print(f"{arr[j]} and {arr[j+1]} have swapped places.")
    
    if not swapped:
        print("No swaps were made. List is already sorted.")
        break  # Stop if already sorted

    else:
        print(f"Pass {i + 1}: {arr}")

print("Sorted list:", arr)

