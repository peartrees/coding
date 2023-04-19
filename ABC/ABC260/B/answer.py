n, x, y, z = map(int, input().split())
math = input().split()
eng = input().split()


result = []

score_list = []
for i, mat , en in zip(range(1, n+1), math, eng):
    score_list.append((i, mat, en))

score_list = sorted(score_list, key=lambda x: (x[1]), reverse=True)

for i in range(x):
    result.append(score_list[0][0])
    del score_list[0]

score_list = sorted(score_list, key=lambda x: (x[2]), reverse=True)

for j in range(y):
    if score_list[0][2] == score_list[1][2]:
        if score_list[0][0] > score_list[1][0]:
            result.append(score_list[1][0])
            del score_list[1]
        else:
            result.append(score_list[0][0])
            del score_list[0]
    else:
        result.append(score_list[0][0])
        del score_list[0]


for k in range(len(score_list)):
    score_sum = (int(score_list[k][1]) + int(score_list[k][2]))
    score_list[k] = (score_list[k][0], score_list[k][1], score_list[k][2], score_sum)


sum_score_list = sorted(score_list, key=lambda x: (x[3], x[0]), reverse=True)

for l in range(z):

    if (len(sum_score_list) > 2) and (sum_score_list[0][3] == sum_score_list[1][3]):
        if sum_score_list[0][0] > sum_score_list[1][0]:
            result.append(sum_score_list[1][0])
            del score_list[1]
        else:
            result.append(sum_score_list[0][0])
            del score_list[0]

    else:
        result.append(sum_score_list[0][0])
        del sum_score_list[0]


result = sorted(result)

for i in range(len(result)):
    print(result[i])