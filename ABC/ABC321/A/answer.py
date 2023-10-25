N = input()
flg=True
result="Yes"
for i in range(len(N)-1):
    if N[i] <= N[i+1]:
        flg=False
        result = "No"
        print(result)
        break

if flg:
    print(result)
