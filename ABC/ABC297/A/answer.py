n, m = map(int, input().split())
x = list(map(int, input().split()))

ans = -1

for i in range(len(x)-1):
    dist = x[i+1] - x[i] 
    if m >= dist:
        ans = x[i+1]
        break

print(ans)