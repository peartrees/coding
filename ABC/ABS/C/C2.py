S = input()

S = S.replace("eraser", "0")
# print(S)
S = S.replace("erase", "0")
# print(S)
S = S.replace("dreamer", "0")
# print(S)
S = S.replace("dream", "0")
# print(S)
S = S.split("0")
# print(S)
tmp = [a for a in S if a!= ""]
# print(S)

if tmp == []:
    print("YES")
else:
    print("NO")