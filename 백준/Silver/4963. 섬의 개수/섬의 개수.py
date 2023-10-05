import sys
sys.setrecursionlimit(10000)

dy = [1, 1, 1, 0, 0, -1, -1, -1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(y, x):
    for k in range(8):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nx < n and 0 <= ny < m:
            if chk[ny][nx] == False and graph[ny][nx] == 1:
                chk[ny][nx] = True
                dfs(ny, nx)
while True:
    n,m = map(int,input().split())
    if n == 0 and m ==0: 
        break
    else: 
        graph = []
        for i in range(m):
            graph.append(list(map(int,input().split())))

        chk = [[False] * n for _ in range(m)]
        cnt = 0
        # print(graph)
        # print(chk)

        for i in range(m):
            for j in range(n):
                if chk[i][j] == False and graph[i][j] == 1:
                    dfs(i, j)
                    cnt += 1

        print(cnt)