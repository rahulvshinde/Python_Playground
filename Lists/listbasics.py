"""
1. Lists are ordered sequences that can hold a variety of object types.
2. Lists are constructed with brackets [] and commas separating every element in the list.
3. Example, my_list = [1,2,3]
4. Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called
   off of them.
"""

my_nums = [1, 2, 3, 4]

my_strings = ['Rahul', 'Shinde', 'Santa Clara', 95054]

print("My list: {ele} has total {num} elements".format(ele=my_nums, num=len(my_nums)))
########################################################################################

# Indexing and Slicing

my_list = ['one', 'two', 'three', '4', '5']
print(my_list[0])

# Grab index 1 and everything past it
print(my_list[1:])

# Grab everything UP TO index 3
print(my_list[:3])

# Concatenate the string with the list
print(my_list + ['Pune'])
# Note: This doesn't actually change the original list!
########################################################################################

# Basic List Methods
# 1. append()

my_list.append('India')
print(my_list)

# 2. pop()
my_list.pop(4)
print(my_list)

# 3. sort()
my_list.sort()
print(my_list)

# 4. reverse()
my_list.reverse()
print(my_list)
########################################################################################

# Nested Lists
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
matrix = [list1,list2,list3]
print(matrix)

print(matrix[2][1])

first_col = [row[0] for row in matrix]
print("first_col {}".format(first_col))

