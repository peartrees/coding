N = int(input())
A = list(map(int, input().split()))

cnt = 0
flg=False
while True:
    for i in range(N):
        if ((A[i]%2) == 0):
            A[i] = (A[i]/2)
            # print(A[i])
        else:
            flg = True
            break
    if flg:
        break
    else:
        cnt+=1

print(cnt)