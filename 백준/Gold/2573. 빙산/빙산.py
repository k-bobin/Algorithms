from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def count_adjacent_zeros(y, x):
    count = 0
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 0:
            count += 1
    return count

def melt():
    new_maps = [row[:] for row in maps]  # Create a copy of the maps
    for i in range(n):
        for j in range(m):
            if maps[i][j] > 0:
                new_maps[i][j] = max(maps[i][j] - count_adjacent_zeros(i, j), 0)
    return new_maps

def bfs(y, x, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] > 0 and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

year = 0

while True:
    year += 1
    maps = melt()
    
    visited = [[False] * m for _ in range(n)]
    iceberg_count = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                iceberg_count += 1
    
    if iceberg_count == 0:
        print(0)
        break

    if iceberg_count > 1:
        print(year)
        break
