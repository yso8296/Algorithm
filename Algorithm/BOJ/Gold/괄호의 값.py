word = input()
result = 0
score = 1
stack = []

for i in range(len(word)):
  if word[i] == '(':
    score *= 2
    stack.append(word[i])
  elif word[i] == '[':
    score *= 3
    stack.append(word[i])
  elif word[i] == ')':
    if not stack or stack[-1] != '(':
      result = 0
      break
    if word[i - 1] == '(':
      result += score
    score //= 2
    stack.pop()
  elif word[i] == ']':
    if not stack or stack[-1] != '[':
      result = 0
      break
    if word[i - 1] == '[':
      result += score
    score //= 3
    stack.pop()

if stack:
  print(0)
else:
  print(result)