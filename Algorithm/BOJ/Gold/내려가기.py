import copy
n = int(input())
board = list(map(int, input().split()))
small = copy.deepcopy(board)
big = copy.deepcopy(board)

for i in range(n - 1):
  board = list(map(int, input().split()))
  small = [board[0] + min(small[0], small[1]), board[1] + min(small[0], small[1], small[2]), board[2] + min(small[1], small[2])]
  big = [board[0] + max(big[0], big[1]), board[1] + max(big[0], big[1], big[2]), board[2] + max(big[1], big[2])]

print(max(big), min(small))