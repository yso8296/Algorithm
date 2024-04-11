from collections import Counter
name = input()
word = Counter(name)
count = 0
result = ''
mid = ''

for k, v in list(word.items()):
  if v % 2 != 0:
    count += 1
    mid = k
if count > 1:
  print("I'm Sorry Hansoo")
  exit()

for k, v in sorted(word.items()):
  result += (k * (v // 2))
print(result + mid + result[::-1])