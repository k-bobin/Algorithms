# 1303 전투
#W가 내편
#W의 숫자에서 제곱 
from collections import deque

#dfs 함수 생성
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def bfs(y, x, word):
    rs =1
    q = deque()
    q.append((y,x))
    while q: 
        ey,ex = q.popleft()
        for k in range(4):
            ny = ey+ dy[k]
            nx = ex+ dx[k]
            if 0<=ny<m and 0<=nx<n:
                if map[ny][nx] == word and chk[ny][nx] == False:
                    rs +=1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs


#map, chk 만들기 
n,m= map(int, input().split())
map= []
for _ in range(m):
    temp = list(input())  # 수정: 리스트로 입력 받기
    map.append(temp)
chk = [[False]*n for _ in range(m)]
your_power = 0
enemy_power = 0

for i in range(m):
    for j in range(n):
        if map[i][j] == "W" and chk[i][j] == False:
            chk[i][j] = True
            your_power += (bfs(i,j,"W")**2)
        elif map[i][j] =="B" and chk[i][j] == False:
            chk[i][j] = True
            enemy_power += (bfs(i,j,"B")**2)
        
print(your_power, enemy_power)

