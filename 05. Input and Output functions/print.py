# Print nothing
print()

# Print a string
print('Hello' * 3)

# Prints to a new line always
print('All the power is within you')

a, b = 10, 20

# Print variables with separator
print(a, b, sep=',')

name = 'John'
marks = 94.5678

print('Name is ', name, '. Marks are ', marks)
print('Name is %s, Marks are %.2f' % (name, marks))
print('Name is {}, Marks are {}'.format(name, marks))
print('Name is {0}, Marks are {1}'.format(name, marks))
