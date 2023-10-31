N = int(input())
ls = [int(x) for x in input().split()]

ls.sort()
# print(ls)
start = ls[0]

for i in range(N+1):
    if ls[i] != start:
        print(start)
        break
    else:
        start += 1