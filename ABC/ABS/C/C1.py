N, Y = map(int, input().split())

flg=False
z_tmp = Y//10000

for i in range(0, z_tmp+1):
    yukiti = 10000*i
    for j in range(0, N-i+1):
        fuku = 5000*j
        k = N-i-j
        nogu = 1000*k
        if (yukiti+fuku+nogu==Y):
            print(i, j, k)
            flg=True
            break
    if flg:
        break

if flg==False:
    print(-1, -1, -1)