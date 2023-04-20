N, A, B = map(int, input().split())

ans = []

for i in range(N+1):
    s = str(i)
    S = list(map(int, s))
    total = sum(S)
    if total>=A and total<=B:
        ans.append(i)

# print(ans)
print(sum(ans))