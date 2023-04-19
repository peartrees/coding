Q = int(input())
Q_ls = [list(map(int, input().split())) for l in range(Q)]

s = 1

for q in Q_ls:
    tmp = q[0]
    if tmp == 3:
        print(s%998244353)
    elif tmp == 1:
        s = s*10 + q[1]
    else:
        tmp_2 = str(s)[1:]
        s = int(tmp_2)

    