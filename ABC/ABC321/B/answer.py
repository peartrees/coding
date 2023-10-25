#!/usr/bin/env python3
N, X = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
l = A[0]
h = A[-1]
s = sum(A)

if s-h >= X:
    print(0)
    exit()

tmp = X-s+l+h

if tmp > h:
    print(-1)

else:
    print(tmp)
