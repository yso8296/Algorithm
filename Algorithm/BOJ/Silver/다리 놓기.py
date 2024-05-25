t = int(input())

def factorial(num):
  result = 1
  for i in range(1, num + 1):
    result *= i
  return result

for _ in range(t):
  n, m = map(int, input().split())
  print(int(factorial(m) / (factorial(m - n) * factorial(n))))
