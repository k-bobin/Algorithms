from collections import deque

t = int(input())
for _ in range(t):
    l = int(input())  # 체스판의 크기 l을 입력 받음
    graph = [[False] * l for _ in range(l)]
    sx, sy = map(int, input().split())  # 시작 위치 입력 받음
    ex, ey = map(int, input().split())  # 목표 위치 입력 받음

    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]

    graph[sy][sx] = 0

    q = deque()
    q.append((sx, sy))

    while q:
        sx, sy = q.popleft()
        if sx == ex and sy == ey:
            break

        for k in range(8):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0 <= nx < l and 0 <= ny < l and graph[ny][nx] == False:
                graph[ny][nx] = graph[sy][sx] + 1
                q.append((nx, ny))

    print(graph[ey][ex])
