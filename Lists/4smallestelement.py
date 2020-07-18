# 4. Write a Python program to get the smallest number from a list.

my_list = [1, 2, 5, -6, 8, 0]


def smallest_element(my_list):
    smallest = my_list[0]
    for item in my_list:
        if smallest >= item:
            smallest = item
    return smallest


print("Smallest Element in the list: {} is {}".format(my_list, smallest_element(my_list)))
