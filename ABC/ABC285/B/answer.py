n = int(input())
s = input()

for i in range(1,n):
    cnt = 0
    flg=True
    for j in range(n-i):
        if (s[j] != s[j+i]):
            cnt += 1
        else:
            print(j)
            flg = False
            break
    if flg:
        print(cnt)