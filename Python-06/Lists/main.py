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

List = [1, 2, 4, 6, 7]
List.append(9)
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
print(Listnum)

# Remove
Listnum = [1, 2, 3]



