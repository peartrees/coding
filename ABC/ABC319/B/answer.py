N = int(input())

def divisors_list(num):
    divisors = []
    for i in range(1, 10):
        if num % i == 0:
            divisors.append(i)
    return divisors

div_ls = divisors_list(N)
ans = []
ans.append(min(div_ls))

for i in range(1,N+1):
    flg=True
    for num in div_ls:
        if (i%(N/num)==0):
            ans.append(str(num))
            flg=False
            break
    if flg:
        ans.append("-")

print("".join(str(item) for item in ans))
