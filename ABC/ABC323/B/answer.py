N = int(input())
s_ls = []
for _ in range(N):
    s_ls.append(input())

result_dict = {}

for i in range(N):
    cnt = 0
    for j in range(N):
        if s_ls[i][j] ==  "o":
            cnt += 1
    result_dict[i+1] = cnt

result_dict = sorted(result_dict.items(),
                     key=lambda score :score[1],
                     reverse=True)
ans=[]
for i in range(N):
    ans.append(result_dict[i][0])

print(*ans)
