s = input()

omoji = [chr(i) for i in range(65,91)]
# print(omoji)

result = 0
for i in range(len(s)):
    banme = len(s)-i
    tmp = ord(s[i])-64
    # print(tmp)
    result += (tmp * 26**(banme-1))
print(result)
