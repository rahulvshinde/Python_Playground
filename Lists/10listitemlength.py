# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

my_list = ['RahulShinde', 'Rahul', 'California', '10', 'San Mateo', 'Chico']


def listitemlen(n, my_list):
    new_list = []
    for item in my_list:
        if len(item) > 5:
            new_list.append(item)
    return new_list


print("List of items whose length is greater than {n}: {l}".format(n=5, l=listitemlen(5, my_list)))
