import sys
sys.setrecursionlimit(10000)
from collections import deque

#함수 생성
def bfs(y,x): 
    q = deque()
    q.append((y,x))
    while q: 
        y,x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny,nx))



T = int(input())

for _ in range(T):
    M,N,K = map(int, input().split())   #가로, 세로, 위치개수
    graph = [[0]* M for _ in range(N)]
    chk = [[False]* M for _ in range(N)]
    cnt = 0

    dy = [1,0, -1, 0]
    dx = [0,1,0,-1]

    #배추심은곳 1로 변경
    for _ in range(K):
        a,b = map(int, input().split())
        graph[b][a] = 1 

    # 탐색
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and chk[i][j] == False:
                chk[i][j] =True
                bfs(i,j)
                cnt +=1

    print(cnt)