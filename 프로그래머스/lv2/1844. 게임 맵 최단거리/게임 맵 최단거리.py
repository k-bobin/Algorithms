from collections import deque 

def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    chk = [[-1] *m for _ in range(n)]
    
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    def bfs(y,x):
        q= deque()
        q.append((y,x))
        
        while q:
            y,x = q.popleft()
            if y == n-1 and x == m-1:
                return chk[n-1][m-1]
            
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0<=ny<n and 0<=nx<m:
                    if chk[ny][nx] == -1 and maps[ny][nx]== 1:
                        chk[ny][nx] = chk[y][x] + 1 
                        q.append((ny,nx))
        return -1
        
    chk[0][0] =1
    answer = bfs(0,0)
        
    return answer