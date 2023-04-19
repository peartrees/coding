import numpy as np

N = int(input())

A = [list(map(int, input().split())) for l in range(N)]
B = [list(map(int, input().split())) for l in range(N)]

A_ = np.array(A)
B_ = np.array(B)

for i in range(4):
    if np.min(B_ - A_) >= 0:
        ans = "Yes"
        break
    else:
        ans = "No"
        A_ = np.rot90(A_)

print(ans)