N = int(input())
D = [int(input()) for _ in range(N)]

D_sort = sorted(D, reverse=True)
cnt = 1

for i in range(1, N):
    if (D_sort[i-1] > D_sort[i]):
        cnt+=1

print(cnt)
    