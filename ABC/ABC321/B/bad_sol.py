n, x = map(int, input().split())
a_ls = [int(x) for x in input().split()]

a_sort = sorted(a_ls)
# print(a_sort)

# minよりも小さい値を追加する場合:
apd_min = sum(a_sort[0:-1])
# print(apd_min)
apd_max = sum(a_sort[1:])
# print(apd_max)
apd_mid = sum(a_sort[1:-1])
# print(apd_mid)

ans_1, ans_2, ans_3 = -1, -1, -1

if apd_min >= x:
    ans_1 = x-a_sort[0]
    # print(ans_1)

# maxよりも大きい値を追加する場合:
if apd_max >= x:
    ans_2 = a_sort[-1]
    # print(ans_2)

if apd_mid <= x:
    ans_3 = (x - apd_mid)
    if (ans_3 < a_sort[0]) or (ans_3 > a_sort[-1]):
        ans_3 = -1

ans_ls = sorted([ans_1, ans_2, ans_3])
flg=True
for num in ans_ls:
    if (num>=0) and (num<101):
        print(num)
        flg=False
        break
if flg:
    print(-1)
