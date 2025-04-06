
# 🧠 How It Works (Step-by-Step):
# Start at the first element of the list.

# Compare the current element with the target value.

# If they match, you found the value, and the search ends.

# If they don't match, move to the next element.

# Repeat steps 2–4 until:

# You find the target value (success), or

# You reach the end of the list without finding it (failure).

# 📌 Example:
# Suppose you have this list:

# [4, 7, 2, 9, 5]

# And you're searching for 9.

# Check 4 → not a match

# Check 7 → not a match

# Check 2 → not a match

# Check 9 → it's a match! 🎉

# So, the search stops here.

# ✅ Advantages:
# Very simple to understand and implement.

# Works on unsorted lists (no need to sort the data).

# ❌ Disadvantages:
# Can be slow for large lists, since it might need to check every element.

arr = list(map(int,input("The numbers:").split(',')))

size = len(arr)

Find = int(input("You have to find:"))
found = 0
for i in range(size):
    if arr[i] == Find:
        index = i+1
        found = 1
        break

if found == 1:
    print(f"{Find} is the {index}th number of the list.")

else:
    print(Find,"is not found")