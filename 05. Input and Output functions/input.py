# Take input and print it
s = input()
print(s)

# Take input with some text
s = input('Enter your name: ')
print(s)

# Take input as integer
i = int(input('Enter an integer number'))
print(i)
print(type(i))

# Take multiple inputs
lst = [int(x) for x in input('Enter three numbers (separated by comma): ').split(',')]
print(lst)
