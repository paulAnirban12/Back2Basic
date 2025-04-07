
# Unsorted List:
# [5, 3, 8, 4, 2]

# Step 1: Choose a Pivot
# Let's pick 4 as the pivot.

# Step 2: Partitioning
# Elements less than 4 → [3, 2]

# Pivot → [4]

# Elements greater than 4 → [5, 8]

# Now, the array is: [3, 2] + [4] + [5, 8]

# Step 3: Recursively Apply Quick Sort
# Sort [3, 2] → Becomes [2, 3]

# [4] is already sorted.

# Sort [5, 8] → Already sorted.

# ✅ Final Sorted List: [2, 3, 4, 5, 8]

# Time Complexity
# Best/Average Case: O(n log n)

# Worst Case (if poorly chosen pivot): O(n²)

# Key Points
# ✔️ Faster than Bubble, Selection, and Insertion Sort for large datasets.
# ✔️ Efficient for most cases, but worst case happens if pivot selection is bad (e.g., already sorted data with first element as pivot).
def Partition(array,low,high):

    pivot = array[high]

    i = low-1

    for j in range(low,high):
        if array[j]<=pivot:
            i += 1
            array[i],array[j] = array[j],array[i]

    array[high],array[i+1] = array[i+1],array[high]

    return i+1

def quicksort(array,low,high):
    if low < high:
        pivot_index = Partition(array,low,high)
        quicksort(array,low,pivot_index-1) 
        quicksort(array,pivot_index+1,high) 
    
    return array


arr = list(map(int,input("Unsorted List:").split(',')))
low = 0
high = len(arr)-1
arr = quicksort(arr,low,high)
print("High =",arr[high],"and low = ",arr[low])
print("Sorted List:",arr)
