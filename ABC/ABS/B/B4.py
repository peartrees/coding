N = int(input())
A = list(map(int, input().split()))

A_sort = sorted(A, reverse=True)
# print(A_sort)

Alice_total = 0
Bob_total = 0

for i in range(N):
    if i%2 == 0:
        Alice_total += A_sort[i]
    else:
        Bob_total += A_sort[i]

print(Alice_total-Bob_total)
