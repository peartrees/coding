N, Y = map(int, input().split())

flg=False
z_tmp = Y//10000

for i in range(z_tmp, 0, -1):
    yukiti = 10000*i
    for j in range(N-i, 0, -1):
        fuku = 5000*j
        for k in range(N-i-j, 0, -1):
            nogu = 1000*k
            print(i,j,k)
            if (yukiti+fuku+nogu==Y):
                print(i, j, k)
                flg=True
                break
        if flg:
            break
    if flg:
        break

# if flg==False:
#     print(-1, -1, -1)