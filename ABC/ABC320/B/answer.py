#
# # ダメなコード
# s = input()
# cnt = 0
# for i in range(len(s)):
#     # i文字目開始の回文判定
#     for j in range(i,len(s)):
#         tmp=0
#         # print(i,j)
#         seg = s[i:j+1]
#         print(seg)
#         if (seg == seg[::-1]):
#             tmp = len(seg)
#             if tmp > cnt:
#                 cnt = tmp
#         # print(cnt)
# print(cnt)

s = input()
cnt = 0
for i in range(len(s)):
    # i文字目開始の回文判定
    for j in range(i, len(s)):
        seg = s[i:j+1]
        if seg == seg[::-1]:  # 正しい回文の判定方法
            tmp = len(seg)
            if tmp > cnt:
                cnt = tmp
print(cnt)
