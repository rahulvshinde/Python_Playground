"""82. Write a Python program to generate the combinations of n distinct objects taken from the elements of
a given list.
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
"""

import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combine_list = []


def combinelist(my_list):
    for i in range(len(my_list)):
        for ctr in range(len(my_list)):
            if i is not ctr and ctr>i:
                new_entry = [my_list[i], my_list[ctr]]
                combine_list.append(new_entry)

    return combine_list


print("My List: {}".format(my_list))
print("Combination List: {}".format(combinelist(my_list)))
