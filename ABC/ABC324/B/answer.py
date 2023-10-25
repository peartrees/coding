N = int(input())

import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
c = collections.Counter(prime_factorize(N))
result = list(c.keys())

flg=True
for i in range(len(result)):
    if (result[i] != 2) and (result[i] != 3):
        print("No")
        flg=False
        break

if flg:
    print("Yes")
