N = int(input())
S = input()
flg=False

for i in range(0, N-2):
    if S[i:i+3] == "ABC":
        print(i+1)
        flg=True
        break

if flg==False:
    print(-1)
