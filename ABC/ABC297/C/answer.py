H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

for i in range(len(S)):
    s = S[i]
    print(s)
    for w in range(1, W, 2):
        if (s[w-1] == "T") and (s[w] == "T"):
            print("OK")
            s = s[w-2] + "PC" + s[w]
            print(s)



# for s in S:
#     print(s)