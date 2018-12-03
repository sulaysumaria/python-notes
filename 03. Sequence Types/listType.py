# Create empty list
lst = []
print(lst)

# Create list with data
lst = [10, 20, 'Sulay', -10, 30.5]
print(lst)

# Indexing
print(lst[3])

# Slicing
print(lst[3:5])

# Repitition
print(lst * 4)

# Length
print(len(lst))

# Add element
lst.append(40)
print(lst)

# Remove element
lst.remove('Sulay') # Case sensitive
print(lst)

# Remove by index
del(lst[1])
print(lst)

# Get maximum element
print(max(lst))

# Get minimum element
print(min(lst))

# Insert element at particular position
lst.insert(3, 99) # inserts 99 at index 3

# Sort list, default ascending
lst.sort()
print(lst)

# Sort in descending
lst.sort(reverse=True)

# Remove all elements from list
lst.clear()
print(lst)
