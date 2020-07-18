# 1. Write a Python program to sum all the items in a list.

my_list = [1,2,3,4]
print(sum(my_list))

def sum_list(my_list):
    total_items = 0
    for item in my_list:
        total_items += item
    return total_items
print("Total of all elements in the list is {}".format(sum_list(my_list)))
