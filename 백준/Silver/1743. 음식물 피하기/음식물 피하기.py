import sys
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nx < m+1 and 0 <= ny < n+1:
            if chk[ny][nx] == False and maps[ny][nx] == 1:
                chk[ny][nx] = True
                dfs(ny, nx)

n, m, k = map(int, sys.stdin.readline().split())
chk = [[False] * (m + 1) for _ in range(n + 1)]
maps = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    maps[r][c] = 1

num = 1
for j in range(1, n + 1):
    for i in range(1, m + 1):
        if maps[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            num = max(num, each)

print(num)
