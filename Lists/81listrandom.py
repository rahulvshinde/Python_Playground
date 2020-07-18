"""81. Write a Python program to extract a given number of randomly selected elements from a given list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the above list:
[4, 4, 1]"""

import random
my_list = [1, 1, 2, 3, 4, 4, 5, 1]
ran_list = []
def randomlist(my_list,n):
    for i in range(n):
        ran_list.append(my_list[random.randint(0,len(my_list)-1)])
    return ran_list
print("Random List: {}".format(randomlist(my_list,3)))


# def random_select_nums(n_list, n):
#     return random.sample(n_list, n)
#
#
# n_list = [1, 1, 2, 3, 4, 4, 5, 1]
# print("Original list:")
# print(n_list)
# selec_nums = 3
# result = random_select_nums(n_list, selec_nums)
# print("\nSelected 3 random numbers of the above list:")
# print(result)