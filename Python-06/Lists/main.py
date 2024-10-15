# what is lists ?

# creating a list
L = ['20', '24', '30', '45', '56', '67', '54']
print(L)

# id shows the memory address of data-types
num = [1, 2, 3]

print(id(num))
print(id(num[0]))
print(id(num[1]))
print(id(num[2]))
print(id(1))
print(id(2))
print(id(3))

# lists examples

L = [2, 4, 6]
print(L)
L_2D = [1, 2, 3, [6, 7, 8]]
print(L_2D)
L_3D = [[[1, 2, 3]], [[4, 5]], [[7, 8, 9]]]
print(L_3D)

# Accessing the lists

# Indexing
nums = [1, 2, 3, 4]
print(nums[0])
print(nums[3])
print(nums[-1])
print(nums[-2])

# Slicing

L = [1, 2, 3, 4, 5]
print(L[0:3])
print(L[0::2])

# Reverse a list
print(L[::-1])

# Add an item in list

List = [1, 2, 4, 6, 7, 9]
# print(List)

# here the func insert the list in list instead of numbers
List.extend([10, 12, 14])
print(List)

# Here the extend func use the index of the string
List.extend('mumbai')
print(List)

# here the insert func takes an index positions
# and an element you want to insert in a list
List.insert(2, 3)
print(List)

# Editing items in a list
# as a list is a mutable data-type then we can edit the list easily

# Editing with indexing
List[-1] = 16
print(List)

# Editing with slicing
Lists = [100, 2, 3, 4, 500]
Lists[1:4] = [200, 300, 400]
print(Lists)

# Deleting an items of list
Listnum = [1, 2, 3]
print(Listnum)

# Deleting the list
del Listnum
# print(Listnum)

# Remove
Listnum = [1, 2, 3]
Listnum.remove(3)
print(Listnum)

# pop
Listnum = [1, 2, 3, 4, 5, 6]
Listnum.pop()
print(Listnum)

# clear
Listnum = [1, 2, 3, 4, 5, 6]
Listnum.clear()
print(Listnum)

# Operators on lists

# Arithmetic (+ ,*)

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

# Concatenation/Merge
print(L1 + L2)

L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, [5, 6]]

print(5 not in L1)
print([5, 6] in L2)

# Loops

for i in L1:
    print(i, end=' ')
print()

for i in L2:
    print(i, end=' ')
print()

# List functions

# Len
print(len(L1))
print(len(L2))

# Count
print(L1.count(4))

# index
print(L2.index(2))

# copy
print(L1.copy())

# List Comprehension
# provides a concise way of creating lists.

# Advantages of List Comprehension

# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.

# Add 1 to 10 numbers to a list

L = []

for i in range(1, 11):
    L.append(i)

print(L)

L = [i for i in range(1, 11)]
print(L)

# Print all numbers divisible by 5 in the range of 1 to 50
L = [i for i in range(1, 51) if i % 5 == 0]
print(L)

# find languages which start with letter p
languages = ['java', 'python', 'php', 'c', 'javascript']

var = [language for language in languages if language.startswith('p')]
print(var)

# Nested if with List Comprehension
basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']

var1 = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]

print(var1)

# Print a (3,3) matrix using list comprehension -> Nested List comprehension
var2 = [[i * j for i in range(1, 4)] for j in range(1, 4)]

print(var2)

# cartesian products -> List comprehension on 2 lists together
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

var3 = [i*j for i in L1 for j in L2]


# 2 ways to traverse a list
# item-wise
# index-wise


L = [1, 2, 3, 4]

for i in range(0, len(L)):
    print(i, end=" ")



