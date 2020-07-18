import collections

test_list = [{"Akash": 1}, {"Kil": 2}, {"Akshat": 3}, {"Kil": 2}, {"Akshat": 3}]
# print (test_list)

uni_list = []
for i in range(len(test_list)):
    if test_list[i] not in test_list[i + 1:]:
        print(test_list[i + 1:])
        uni_list.append(test_list[i])

# print(uni_list)

seen = set()
new_l = []
for d in test_list:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)

print (new_l)