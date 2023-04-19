t = int(input())
prob_list = []
for _ in range(t):
    n = int(input())
    for i in range(n):
        prob_list.append(input().split())
        # print(prob_list)
        break

for prob in prob_list:
    cnt = 0
    for num in prob:
        if (int(num) % 2) == 1:
            cnt += 1
    print(cnt)