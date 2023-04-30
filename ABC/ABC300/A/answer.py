N, A, B = map(int, input().split())
C = list(map(int, input().split()))

total = A+B
for i in range(N):
    if C[i] == total:
        print(i+1)
        break