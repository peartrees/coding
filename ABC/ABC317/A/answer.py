n, h, x = (int(x) for x in input().split())
p_ls = [int(x) for x in input().split()]

for i in range(n):
    tmp = h + p_ls[i]
    if tmp >= x:
        print(i+1)
        break
