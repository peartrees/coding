N = int(input())
ls = []
for i in range(N):
    w,x  = map(int, input().split())
    x += 9
    ls.append([w,x])

# print(ls)

ans = {}

# 全探索する
for i in range(23):
    # print(f"\n{i}時間目")
    ans[i] = 0
    for j in range(N):
        # print(ls[j])
        start = ls[j][1]+i
        if start >= 24:
            start -= 24
        end = start+1
        # print(start, end)
        if ((start >= 9) and (end <= 18)):
            ans[i] += ls[j][0]
    # print(ans[i])

print(max(ans.values()))