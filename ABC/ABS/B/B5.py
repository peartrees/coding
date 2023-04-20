A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0

for i in range(A+1):
    num_500 = i
    for j in range(B+1):
        num_100 = j
        for k in range(C+1):
            num_50 = k
            ALL = (500*num_500 + 100*num_100 + 50*num_50)
            if (ALL == X):
                cnt+=1
print(cnt)