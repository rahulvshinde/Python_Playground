"""72. Write a Python program to flatten a given nested list structure.
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]"""

my_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flat_list = []


def flatmylist(my_list):
    for item in my_list:
        if isinstance(item, list):
            flatmylist(item)
        else:
            flat_list.append(item)
    return flat_list


print("Original List: {}".format(my_list))
print("Flatted List: {}".format(flatmylist(my_list)))
