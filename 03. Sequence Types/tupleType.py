# Empty tuple
tpl = ()
print(tpl)

# Tuple with values
tpl1 = (40, 50, 40, 'XYZ')
print(tpl1)

# If only one element, trailing comma is compulsary
tpl2 = (40,)
print(tpl2)

# Indexing
print(tpl1[3])

# Repitition
print(tpl * 3)

# Count
print(tpl.count(40))

# Find index
print(tpl.index('XYZ'))

# Convert list ot tuple
lst = [67, 34, 'XYZ']
print(lst)
print(type(lst))

tpl3 = tuple(lst)
print(tpl3)
print(type(tpl3))
