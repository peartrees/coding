S = input()

for i in range(1,16+1,2):
    if (S[i] == "0"):
        flg=True
    else:
        flg=False
        break

if flg:
    print("Yes")
else:
    print("No")
