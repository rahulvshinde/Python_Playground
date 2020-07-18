# 8. Write a Python program to check a list is empty or not.

my_list = []


def emptylist(my_list):
    checkitem = "Not Empty"
    if not my_list:
        checkitem = "Empty"
    return checkitem


print("List is {}.".format(emptylist(my_list)))
