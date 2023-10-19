ls = list(map(int, input().split()))

n, m, p = ls[0], ls[1], ls[2]
cnt = m
cnt2 = 0
while cnt<=n:
    cnt2 += 1
    cnt = cnt+p
print(cnt2)
