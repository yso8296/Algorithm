n, k = map(int, input().split())
s = input()
eat = [0] * n
result = 0

for i in range(n):
  if s[i] == 'H':
    continue
  check = False
  for j in range(k):
    idx = i - (k - j)
    if idx >= 0 and s[idx] == 'H' and not eat[idx]:
      result += 1
      eat[idx] = 1
      check = True
      break
  if check:
    continue
  for j in range(k):
    idx = i + j + 1
    if idx < n and s[idx] == 'H' and not eat[idx]:
      result += 1
      eat[idx] = 1
      break

print(result)
