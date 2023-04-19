N = int(input())
W = list(input().split())
flg = True

for i in range(N):
    if (W[i] in ["and", "not", "that", "the", "you"]):
        print("Yes")
        flg=False
        break

if flg:
    print("No")