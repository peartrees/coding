n = int(input())
name_list = []
for _ in range(n):
    name_list.append(input())

for i in range(len(name_list)-1, -1, -1):
    print(name_list[i])
