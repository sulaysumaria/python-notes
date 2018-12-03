lst = [20, 30, 40, 234]
print(type(lst))

# Convert list to bytes
b = bytes(lst)
print(type(b))

# Cannot add elements to bytes

# Convert to bytearray
b1 = bytearray(lst)
print(type(b1))

# Add element to bytearray
b1[2] = 33
