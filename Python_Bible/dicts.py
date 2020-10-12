students={
    "male" : ["raj","ramesh","sameer","tom","charlie"],
    "female" : ["rutu","rupali","suchita","sonali","deepali"]
}

for key in students.keys():
    for name in students[key]:
        if "a" not in name:
            print(name)


even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)