s = {10, 20, 'XYZ'}
print(s)
print(type(s))

# No duplicates allowed
s1 = {10, 20, 'XYZ', 10, 20}
print(s1)
print(type(s1))

# Update set
s.update([88, 99])
print(s)
print(type(s))

# Removing
s.remove(30)
print(s)

# Cannot perform indexing, slicing or repitition

# Frrezing the set
f = frozenset(s)

# cannot update or remove from frozen set
