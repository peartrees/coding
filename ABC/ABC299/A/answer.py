N = int(input())
S = input()

index_1st = S.index("|")
index_3rd = S.rindex("|")
target_index = S.index("*")

if (index_1st < target_index) and (target_index < index_3rd):
    print("in")
else:
    print("out")