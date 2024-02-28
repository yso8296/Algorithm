dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(board, h, w):
    color = board[h][w]
    count = 0
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
            continue
        if board[nx][ny] != color:
            continue
        count += 1
    return count