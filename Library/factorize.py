def factorize(x):
  nums = []
  for i in range(2, x+1):
      while x % i==0:
        nums.append(i)
        x = x / i
  return nums
