N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(101):
    A.append(i)
    A.sort()
    h = A[0]
    l = A[-1]
    total = sum(A)-h-l
    if total >= X:
        print(i)
        flg=False
        break
    else:
        A.remove(i)
        flg=True

if flg:
    print(-1)
