N = int(input())
S = input()

flg = True

for i in range(N-1):
    if ((S[i]+S[i+1]) == ("MM") or ((S[i]+S[i+1]) == "FF")):
        print("No")
        flg = False
        break

if (flg == True):
    print("Yes")