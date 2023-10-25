n, m = map(int, input().split())
s = input()
t = input()

window = len(s)
# print(t[-window:])

# 接頭辞，接尾辞判定
if t[0:window] == s:
    if t[-window:] == s:
        print(0)
    else:
        print(1)
elif t[-window:] == s:
    print(2)
else:
    print(3)
