N = int(input())
a_ls = [int(x) for x in input().split()]

for i in range(N-1):
    if a_ls[i] != a_ls[i+1]:
        flg=False
        break
    else:
        flg=True

if flg:
    print("Yes")
else:
    print("No")
