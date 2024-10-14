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