from collections import deque 

def solution(maps):
    answer = []
    n,m = len(maps), len(maps[0])
    chk = [[False] *m for _ in range(n)]
    
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    def bfs(y,x,total):
        q =deque()
        q.append((y,x))
        
        while q:
            y,x = q.popleft()
            for k in range(4):
                ny = y+dy[k]
                nx = x+dx[k]
                if 0<=ny<n and 0<=nx<m:
                    if maps[ny][nx] != 'X' and chk[ny][nx] == False:
                        chk[ny][nx] = True
                        total += int(maps[ny][nx])
                        q.append((ny,nx))
        return total                

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and chk[i][j] == False:
                chk[i][j] = True
                rs = int(maps[i][j])
                answer.append(bfs(i,j,rs))
    
    if len(answer):
        answer.sort()
        return answer
    else:
        return [-1]
