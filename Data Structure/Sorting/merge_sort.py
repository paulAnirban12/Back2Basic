# How It Works
# Divide – Recursively split the array into two halves until each subarray has one element.

# Conquer – Sort each half separately (since a single element is already sorted).

# Merge – Combine the two sorted halves into a single sorted array.

# Example
# Unsorted List:
# [5, 3, 8, 4, 2]

# Step 1: Divide
# Split into [5, 3, 8] and [4, 2]

# Split further:

# [5, 3, 8] → [5] and [3, 8] → [3] and [8]

# [4, 2] → [4] and [2]

# Step 2: Conquer (Sort Small Parts)
# Each subarray is now [5], [3], [8], [4], [2] (all single elements, so they are already sorted).

# Step 3: Merge
# Merge [3] and [8] → [3, 8]

# Merge [5] and [3, 8] → [3, 5, 8]

# Merge [4] and [2] → [2, 4]

# Merge [3, 5, 8] and [2, 4] → [2, 3, 4, 5, 8]

# ✅ Final Sorted List: [2, 3, 4, 5, 8]

# Time Complexity
# Best, Worst & Average Case: O(n log n)

# Space Complexity: O(n) (uses extra space for merging)

# Key Points
# ✔️ Stable sorting algorithm (preserves order of equal elements).
# ✔️ Great for large datasets but uses extra memory.
# ✔️ Faster than O(n²) algorithms like Bubble, Selection, and Insertion Sort.
from math import floor

def merge(array1,array2):

    sorted = []
    while(len(array1)!=0 and len(array2)!=0):
        if array1[0] > array2[0]:
            out = array2[0]
            sorted.append(array2[0])
            array2.remove(out)
        else:
            out = array1[0]
            sorted.append(array1[0])
            array1.remove(out)

    while len(array1) != 0:
        ele = array1[0]
        sorted.append(ele)
        array1.remove(ele)

    while len(array2) != 0:
        ele = array2[0]
        sorted.append(ele)
        array2.remove(ele)

    return sorted

def mergesort(a):
    size = len(a)
    if size == 1:
        return a
    mid = size//2
    array1, array2 = a[:mid],a[mid:]
    
    array1 = mergesort(array1)
    array2 = mergesort(array2)

    return merge(array1,array2)

arr = list(map(int,input("Unsorted List:").split(',')))
arr = mergesort(arr)

print("Sorted List:",arr)


    

