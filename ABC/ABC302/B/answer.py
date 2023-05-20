import numpy as np

R, C = map(int, input().split())
ls = []

for _ in range(R):
    ls.append(input())

# print(ls)

target = "snuke"
target2 = "ekuns"
target_len = len(target)

def find_snuke():
    for i in range(R):
        for j in range(C):
            # 左→右 OK
            if j+target_len<=C and ls[i][j:j+target_len] == target:
                for k in range(target_len):
                    print(i+1, j+k+1)
                
             # 右→左 OK
            if j+target_len<=C and ls[i][j:j+target_len] == target2:
                for k in range(target_len):
                    print(i+1, target_len+j-k)
                
            # 上→下 OK
            if i + target_len <= R:
                found=True
                for k in range(target_len):
                    if ls[i+k][j] != target[k]:
                        found=False
                        break
                if found:
                    for k in range(target_len):
                        print(k+i+1,j+1)

            # 下→上 OK
            if i + target_len <= R:
                found=True
                for k in range(target_len):
                    if ls[i+k][j] != target2[k]:
                        found=False
                        break
                if found:
                    for k in range(target_len):
                        print(target_len+i-k,j+1)

            # 左上→右下 OK
            if i + target_len <= R and j + target_len <= C:
                found = True
                for k in range(target_len):
                    if ls[i+k][j+k] != target[k]:
                        found = False
                        break
                if found:
                    for l in range(target_len):
                        print(i+l+1, j+l+1)

            # 右下→左上 OK
            if i + target_len <= R and j + target_len <= C:
                found = True
                for k in range(target_len):
                    if ls[i+k][j+k] != target2[k]:
                        found = False
                        break
                if found:
                    for l in range(target_len):
                        print(i+k-l+1,j+k-l+1)

            # 右上→左下 OK
            if i + target_len <= R and j - target_len >= -1:
                found = True
                for k in range(target_len):
                    if ls[i+k][j-k] != target[k]:
                        found = False
                        break
                if found:
                    for l in range(target_len):
                        print(i+l+1,j-l+1)

            # 左下→右上 NG
            if i + target_len <= R and j - target_len >= -1:
                found = True
                for k in range(target_len):
                    if ls[i+k][j-k] != target2[k]:
                        found = False
                        break
                if found:
                    for l in range(target_len):
                        print(i+target_len-l,j-k+l+1)
        
find_snuke()
