dict1 = { 1: 'John', 2: 'Bob', 3: 'Bill' }
print(dict1)

# List all items
print(dict1.items())

# List all keys
k = dict1.keys()
for i in keys:
    print(i)

# List all values
v = dict1.values()
for i in v:
    print(i)

# Get single value by key
print(dict1[3])

# delete element from dictionary
del dict1[2]
print(dict1)
