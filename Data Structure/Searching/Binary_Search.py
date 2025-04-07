# # 🧠 How It Works (Step-by-Step):
# Make sure the list is sorted (very important!).

# Look at the middle element of the list.

# Compare it with the target value:

# If it's a match → you're done! ✅

# If the target is less than the middle → repeat the search in the left half.

# If the target is greater than the middle → repeat the search in the right half.

# Keep dividing and checking until you either:

# Find the value (success), or

# Have nothing left to check (failure).

# 📌 Example:
# Suppose you have this sorted list:

# [2, 4, 6, 8, 10, 12, 14]

# And you're searching for 10:

# Look at the middle → 8 (not a match)

# 10 is greater than 8, so look in the right half → [10, 12, 14]

# New middle is 12 → not a match

# 10 is less than 12, so look in the left half → [10]

# Found it! 🎉

# ✅ Advantages:
# Much faster than linear search, especially for large lists.

# Time complexity is O(log n) (logarithmic).

# ❌ Disadvantages:
# The list must be sorted first.

# More complex than linear search.

def binarysearch(array,target):
    left = 0
    right = len(array)-1
    while left <= right:
        indexes = left+right
        mid = indexes//2
        if array[mid] == target:
            return mid
        elif array[mid]<target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = list(map(int,input("Numbers: ").split(',')))

arr = sorted(arr)

Find = int(input("You have to find:"))

found = binarysearch(arr,Find)

if found == -1:
    print(Find,"is not found")
    

else:
    print(f"{Find} is the {found+1}th number of the list.")