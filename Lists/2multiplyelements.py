# 2. Write a Python program to multiplies all the items in a list.
my_lists = [1, 2, 3, 4]


def multiply_elements(my_list):
    double_list = []
    for item in my_list:
        double_list.append(item * 2)
    return double_list


print("Multiply Elements from {} by 2: {}".format(my_lists, multiply_elements(my_lists)))
