# Strings are sequence of Characters
#
# In Python specifically, strings are a sequence of Unicode Characters
#
# - Creating Strings
a = 'hello'
print(a)

# - Accessing SubString from string

# Indexing
string = 'hello world'
print(string[3])

# Negative indexing
print(string[-1])  # it goes right to left
print(string[-5])

# Slicing
print(string[0:5])
print(string[2:3])
print(string[2:])
print(string[:])
print(string[0:8:2])
print(string[6:0:-2])
print(string[6:0:-1])

# reverse a string
print(string[::-1])
print(string[-5::])

# string is immutable
# string = 'H'

# - Operations on Strings

# - Arithmetic Operations
print('delhi' + " " + 'mumbai')
print('hello' * 4)

# - Relational Operations
print('delhi' == 'mumbai')
print('delhi' != 'mumbai')

# Lexicographically ascii numbers logic
print('mumbai' > 'pune')
print('Pune' > 'pune')  # ascii value of 'P' is less than 'p'

# - Logical Operations
# with and , or
print('hello' and 'world')
print('hello' or 'world')
print('' and 'world')
print('' or 'world')
print('hello' and '')
print('hello' or 'world')
print(not 'hello')

# - Loops on Strings
for i in "hello":
    print('pune')

# - Membership Operations

# - String Functions

# Length func for length of string
len(string)

# max func for max number
max(string)

# min func for min number
min(string)

# Capitalize
string.capitalize()

# Title
string.title()

# format
name = "piyush"
gender = "male"

print("Hi my name is {} and my gender is {}".format(name, gender))
