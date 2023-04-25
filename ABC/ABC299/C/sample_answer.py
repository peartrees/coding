N = int(input())
S = input()
# 初期化
ans = 0

# 左→右，右→左のように2回走査するためのfor文
for i in range(2):
    # 初期化
    level=0
    # 文字列を走査していく
    for j in range(N):
        # 文字列の中で-が現れたときに，levelを初期化．
        # 現れない場合は，oなのでlevelを加算する
        if S[j] == "-":
            ans = max(ans, level)
            level = 0
        else:
            level+=1
    # 文字列を反転して逆から走査する
    S = S[::-1]

if ans!=0:
    print(ans)
else:
    print(-1)


