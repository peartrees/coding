import numpy as np

H, W = map(int, input().split())
A = []
B = []

for _ in range(H):
    A.append(list(input().split()))

for _ in range(H):
    B.append(list(input().split()))

ans = "No"
# print(A,B)

for i in range(H):
    A_tmp = A[i:]+A[0:i]
    # print()
    # print(A_tmp)
    for j in range(W):
        if A_tmp==B:
            ans="Yes"
            break
        for k in range(H):
            # print(A_tmp[k])
            # print(A_tmp[k][0])
            # print(A_tmp[k][0][j:]+A_tmp[k][0][0:j])
            A_tmp[k][0] = A_tmp[k][0][j:]+A_tmp[k][0][0:j]
                # A_tmp[j] =
                # A_tmp[j][0] = A_tmp[j][0][j:] + A_tmp[j][0][0:j]
                # print(A_tmp[j][0])
                # A_tmp[j][0] = A_tmp[j:][0]+A_tmp[0:j][0]
        # break
        # print(A_tmp)
        if A_tmp==B:
            ans="Yes"
            break
    print(A_tmp)
    print(B)
    print("")
print(ans)