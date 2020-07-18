import collections


def findDuplicate(paths):
    groups = collections.defaultdict(list)
    for path in paths:
        directory, *files = path.split()
        print(directory)
        if files:
            for file in files:
                name, content = file.split('(')
                content=content[:-1]
                groups[content].append(directory + '/' + name)
        print(groups.values())
        print(groups.keys())
        print(groups.items())
    return [g for g in groups.values() if len(g) > 1]

#
# def findDuplicate(paths):
#     M = collections.defaultdict(list)
#     for line in paths:
#         data = line.split(" ")
#         root = data[0]
#         print(data[1:])
#         for file in data[1:]:
#             name, _, content = file.partition('(')
#             M[content[:-1]].append(root + '/' + name)
#
#     return [x for x in M.values() if len(x) > 1]

print (findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
