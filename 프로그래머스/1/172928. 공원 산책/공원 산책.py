#3:26 -> 3:56
def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    # 시작점 찾기 
    for i in range(n):
        if 'S' in park[i]:
            start_y= i
            for j in range(m):
                if park[i][j] == 'S':
                    start_x = j
    
    park= [list(i) for i in park]
    
    #y,x순
    _dict= {'N':(-1,0), 'E':(0,1), 'W':(0,-1), 'S':(1,0)}
    def movable(y,x,dirs,steps):
        dy, dx = _dict[dirs]
        ny,nx = y,x
        for i in range(steps):
            nny = ny+ dy
            nnx = nx+ dx
            
            if 0<=nny<n and 0<=nnx<m and park[nny][nnx] != 'X':
                ny = nny
                nx = nnx
            else:
                return y,x
            
        return ny,nx
            
    for r in routes: 
        d,s =r.split()
        start_y,start_x= movable(start_y,start_x, d, int(s))
        
        
    return start_y,start_x