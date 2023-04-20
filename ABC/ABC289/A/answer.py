S = input()
ans = ""
for i in range(len(S)):
    if S[i] == "1":
        ans+="0"
    else:
        ans+="1"

print(ans)
