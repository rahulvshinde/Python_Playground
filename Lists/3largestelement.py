# 3. Write a Python program to get the largest number from a list.

my_list = [1, 2, 5, 6, 8, 0]


def largest_element(my_list):
    largest = my_list[0]
    for item in my_list:
        if largest < item:
            largest = item
    return largest


print("Largest Element in the list: {} is {}".format(my_list, largest_element(my_list)))
