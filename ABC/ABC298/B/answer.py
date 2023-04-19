import copy

N = int(input())
A = [list(map(int, input().split())) for l in range(N)]
B = [list(map(int, input().split())) for l in range(N)]


def judge(A, B):
    ans = "No"
    tmp = "True"
    for i in range(N):
        a = A[i]
        b = B[i]
        for j in range(len(a)):
            if (a[j] == 1):
                if b[j] == 0:
                    tmp = False
                    break
        if (tmp == False):
            ans =  "No"
        else:
            ans = "Yes"
    return ans

for _ in range(4):
    A_tmp = copy.deepcopy(A)
    for i in range(N):
        for j in range(N):
            # print(A_tmp[i][j])
            # print("before")
            # print(A_tmp[N-1-j][i])
            # print("")
            tmp_ = A_tmp[N-1-j][i]
            A[i][j] = tmp_
    ans = judge(A,B)
    if ans == "Yes":
        break

ans = judge(A,B)      
print(ans)