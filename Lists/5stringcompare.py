"""
5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last
character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
my_list = ['abc', 'pqr', 'aba', 'pnp', '1201']


def stringcompare(my_list):
    cntr, new_list = 0, []
    for item in my_list:
        if len(item) >= 2:
            if item[0] == item[-1]:
                new_list.append(item)
                cntr += 1
    return cntr


print(stringcompare(my_list))
