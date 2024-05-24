from collections import deque

n = int(input())
arr = list(map(int, input().split()))

def bfs():
    q = deque([(0, 0)]) 
    visited = [False] * n
    visited[0] = True
    
    while q:
        cur, num = q.popleft()
        
        if cur == n - 1:
            return num
        
        for i in range(1, arr[cur] + 1):
            next_pos = cur + i
            if next_pos < n and not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, num + 1))
    
    return -1

print(bfs())