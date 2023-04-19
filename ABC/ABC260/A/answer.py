from collections import Counter

s = list(input())
set_s = set(s)
cnt = Counter(s)

for tmp_s in set_s:
    if (cnt[tmp_s] == 1):
        print(tmp_s)
        flg = False
        break
    else:
        flg = True
if flg:
    print(-1)