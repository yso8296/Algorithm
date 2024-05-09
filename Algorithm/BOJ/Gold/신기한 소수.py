import math
n = int(input())

def isPrime(num):
  if num <= 1:
    return False
  for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        return False
  return True

def solve(num, count):
  if count == n:
    if isPrime(num):
      print(num)
      return
    return
    
  for i in range(0, 10):
    temp = num * 10 + i
    if isPrime(temp):
      solve(temp, count + 1)

solve(0, 0)

  