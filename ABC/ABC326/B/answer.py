N = int(input())

while True:
    s = str(N)
    if int(s[0]) * int(s[1]) == int(s[2]):
        print(N)
        break
    else:
        N += 1