# 7. Write a Python program to remove duplicates from a list.

my_list = [1, 2, 3, 4, 1, 4, 'rahul', 'shinde', 'rahul']

def removeduplicate(my_list):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


print(removeduplicate(my_list))
