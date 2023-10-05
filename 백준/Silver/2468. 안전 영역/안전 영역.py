import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(y, x, h):
    for k in range(4):  # 수정: k를 4로 변경
        ny = y + dy[k]
        nx = x + dx[k]

        if (0 <= nx < N) and (0 <= ny < N):
            if map_data[ny][nx] > h and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx, h)

N = int(input())
map_data = [list(map(int, input().strip().split())) for _ in range(N)]  # 수정: 공백을 기준으로 split
num = 1

for p in range(1, 101):
    chk = [[False] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(N):
            if map_data[j][i] > p and chk[j][i] == False:
                chk[j][i] = True
                dfs(j, i, p)
                cnt += 1  
    num = max(num, cnt)

print(num)
