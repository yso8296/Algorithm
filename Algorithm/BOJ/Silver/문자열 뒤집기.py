s = input()
flip_zero = 0
flip_one = 0
cur = s[0]

if cur == '0':
  flip_one += 1
else:
  flip_zero += 1

for i in range(len(s)):
  if cur != s[i]:
    if cur == '0':
      cur = '1'
      flip_zero += 1
    else:
      cur = '0'
      flip_one += 1

print(min(flip_zero, flip_one))
