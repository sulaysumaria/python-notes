s = '  You are awesome  '
print(s)

s1 = '''You are
the creator
of your destiny'''
print(s1)

# Indexing
print(s[0])
print(s[2])

# Repitition
print(s * 2)

# Length
print(len(s1))
print(len(s))

# Slicing

# starting from 0 to 5
print(s[0:5])

# starting from 0 to end
print(s[0:])

# starting from beginning to 8
print(s[:8])

# starting from last third to last
print(s[-3:-1])

# step values in slicing

# starting from 0 to 9 with increment of 2
print(s[0:9:2])

# starting from 15 to beginning in reverse order
print(s[15::-1])

# reverses the string
print(s[::-1])

# strip the spaces
print(s.strip())

# left strip
print(s.lstrip())

# right strip
print(s.rstrip())

# Find substring, start from 0 to 8
print(s.find('awe', 0, 8))

# Count number of accurrances
print(s.count('a'))

# Replace a substring
print(s.replace('awesome', 'super'))

# Upper case
print(s.upper())

# Lower case
print(s.lower())

# Title case
print(s.title())

a = 10
b = 20.54
c = True
d = 'I am the best'

print(a, b, c, d)
