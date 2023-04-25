N = int(input())
num = [0 for i in range(N)]
for i in range(N):
    print("?", i)
    print("")
    s = int(input())
    num[i] = s
    if len(num)>1:
        if num[i] != num[i+1]:
            print("!", i)
            print("")
            break