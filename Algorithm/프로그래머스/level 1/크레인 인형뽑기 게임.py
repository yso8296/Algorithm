def solution(board, moves):
    basket = []
    height = len(board)
    result = 0
    for move in moves:
        for i in range(height):
            if board[i][move - 1] != 0:
                if len(basket) == 0 or basket[-1] != board[i][move - 1]:
                    basket.append(board[i][move - 1])
                    board[i][move - 1] = 0
                    break
                else:
                    basket.pop()
                    board[i][move - 1] = 0
                    result += 2
                    break
    return result
                
        