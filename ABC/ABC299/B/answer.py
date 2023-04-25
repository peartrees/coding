N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

T_ls = []
flg=False

for i in range(N):
    if C[i] == T:
        T_ls.append(i)
        flg = True


if flg:
    max_num = R[T_ls[0]]
    max_player = 0
    for i in range(len(T_ls)):
        if R[T_ls[i]] >= max_num:
            max_num = R[T_ls[i]]
            max_player = T_ls[i]+1
    # print(max_num)
    print(max_player)
        
else:
    T_ = C[0]
    for i in range(N):
        if C[i] == T_:
            T_ls.append(i)
    max_num = R[T_ls[0]]
    max_player = 0 
    for i in range(len(T_ls)):
        if R[T_ls[i]] >= max_num:
            max_num = R[T_ls[i]]
            max_player = T_ls[i] + 1
    # print(max_num)
    print(max_player)
