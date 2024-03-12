result = 0

def dfs(k, count, dungeons, visited):
    global result
    result = max(result, count)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global result
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return result