n, p, q, r, s = map(int, input().split())
a_list = list(input().split())

result = a_list.copy()
result[p-1:q] = a_list[r-1:s]
result[r-1:s] = a_list[p-1:q]


print(" ".join(result))