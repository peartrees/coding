N = int(input())
S = input()

flg =  False
ans_ls = []
ans = -1

for i in range(N):
    if len(S)==1:
        ans=-1
        break
    s_0 = S[i]
    if s_0=="o":
        for j in range(i,N):
            # print(i,j)
            # print(S[i:j+1])
            # print("check","o"*(len(S[i:j+1])-1)+"-")
            # print("")
            if (S[i:j+1] == "o"*(len(S[i:j+1])-1)+"-"):
                ans_ls.append(len(S[i:j+1])-1)
                flg=True
            else:
                break
    else:
        for j in range(i,N):
            if len(S)==1:
                ans=-1
                break
            # print(i,j)
            # print(S[i:j+1])
            # print("check","-"+"o"*(len(S[i:j+1])-1))
            if (S[i:j+1] == "-"+"o"*(len(S[i:j+1])-1)):
                ans_ls.append(len(S[i:j+1])-1)
                flg=True
            else:
                break


S = S[::-1]
for i in range(N):
    if len(S)==1:
        ans=-1
        break
    s_0 = S[i]
    if s_0=="o":
        for j in range(i,N):
            # print(i,j)
            # print(S[i:j+1])
            # print("check","o"*(len(S[i:j+1])-1)+"-")
            # print("")
            if (S[i:j+1] == "o"*(len(S[i:j+1])-1)+"-"):
                ans_ls.append(len(S[i:j+1])-1)
                flg=True
            else:
                break
    else:
        for j in range(i,N):
            if len(S)==1:
                ans=-1
                break
            # print(i,j)
            # print(S[i:j+1])
            # print("check","-"+"o"*(len(S[i:j+1])-1))
            if (S[i:j+1] == "-"+"o"*(len(S[i:j+1])-1)):
                ans_ls.append(len(S[i:j+1])-1)
                flg=True
            else:
                break

if flg:
    print(max(ans_ls))
else:
    print(ans)