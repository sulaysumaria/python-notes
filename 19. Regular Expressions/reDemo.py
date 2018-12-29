# Sequence Characters

# \d - any digit
# \D - any non digit
# \s - white space
# \S - non white space
# \w - any alpha numeric value
# \W - non alpha numeric value
# \b - space around words
# \A - only at start of string
# \Z - only at end of string

# Quantifiers

# + - one or more repititions
# \d+ - one or more digits
# * - zero or more repititions
# ? - one or more repititions
# {m} - exact m occurrencies
# {m,n} - minimum(default 0), maximum(default infinity)

# Special characters

# \ - escape it with \ character
# . - any character except a new line
# ^ - match at the beginning
# $ - match at the end
# [...] - range of characters
# [^...] - except the range of characters
# (...) - regular expression
# | - multiple regular expression

import re

str = 'Take 1 up 1-3-2019 one 23 idea. one idea 45 at a time 12-11-2020'

# 'o' followed by any two characters
result = re.search(r'o\w\w', str)
print(result.group())

# find all instances
result = re.findall(r'o\w\w', str)
print(result)

# matches only from beginning, start of string
result = re.match(r'T\w\w', str)
print(result.group())

# Split by one or more digits
result = re.split(r'\d+', str)
print(result)

# substitute
result = re.sub(r'one', 'two', str)
print(result)

# find all instances
result = re.findall(r'o\w+', str)
print(result)

# find all instances
result = re.findall(r'o\w*', str)
print(result)

# find all instances
result = re.findall(r'o\w?', str)
print(result)

# find all instances
result = re.findall(r'o\w{1}', str)
print(result)

# find all instances
result = re.findall(r'o\w{1,2}', str)
print(result)

# find all dates
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)

# starts with o
result = re.search(r'^T\w*', str)
print(result.group())
