import collections


# def findDuplicate(paths):
#     M = collections.defaultdict(list)
#     for line in paths:
#         data = line.split()
#         # print (data)
#         root = data[0]
#         # print (root)
#         # print ("File name and Content",data[1:])
#         for file in data[1:]:
#             name, _, content = file.partition('(')
#             # print ("name",name, "_",_,"Content",content)
#             M[content[:-1]].append(root + '/' + name)
#             # print("M",M.values())
#             for i in M.values():
#                 print(i)
#
#     return [x for x in M.values() if len(x) > 1]
def findDuplicate(paths):
    dic = collections.defaultdict(list)
    for path in paths:
        root, *f = path.split(" ")
        for file in f:
            txt, content = file.split("(")
            dic[content] += root + "/" + txt,
    return [dic[key] for key in dic if len(dic[key]) > 1]

print (findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
