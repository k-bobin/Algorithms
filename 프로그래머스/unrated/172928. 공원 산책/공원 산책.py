#4:20
def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                y,x = i,j
                break
    # #y,x순
    direction= {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}
    for i in routes:
        dirs,steps = i.split()
        dy, dx = direction[dirs]
        ny,nx = y,x
        for _ in range(int(steps)):
            #장애물을 만나거나 범위를 벗어난다면 멈추기 
            ny += dy
            nx += dx
            if not (0<=ny<n and 0<=nx<m) or park[ny][nx] == 'X':
                break
        else:
            y = ny
            x = nx
            
    return y,x