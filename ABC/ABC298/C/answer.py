from collections import defaultdict

N = int(input())
box = [[] for i in range(N)]
card = defaultdict(set)
Q = int(input())

for _ in range(Q):
    q = list(map(int, input().split()))
    # print(q)
    if q[0] == 1:
        box_num = int(q[2])
        insert_num = int(q[1])
        box[box_num-1].append(insert_num)
        card[insert_num].add(box_num)

    elif q[0] == 2:
        print(*sorted(box[q[1]-1]))
        # box_num = int(q[1])
        # # print(box_num)
        # num_list = sorted(box[box_num-1])
        # print(*num_list)

    else:
        print(*sorted(card[q[1]]))
        # target = int(q[1])
        # box_num = []
        # for i in range(len(box)):
        #     if target in box[i]:
        #         box_num.append(i+1)
        # box_num = sorted(box_num)
        # print(*box_num)
