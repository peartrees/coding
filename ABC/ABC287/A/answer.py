N = int(input())
cnt_for = 0
for _ in range(N):
    s = input()
    if s == "For":
        cnt_for += 1

cnt_agn =  (N - cnt_for)

if cnt_for > cnt_agn:
    print("Yes")
else:
    print("No")