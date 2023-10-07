#2:00->11
def solution(wallpaper):
    #점 S(lux, luy)에서 점 E(rdx, rdy)로 드래그
    #"드래그 한 거리"는 |rdx - lux| + |rdy - luy|
    #정수 배열 [lux, luy, rdx, rdy]를 return
    answer = []
    #min,min,max,max
    lux,luy, rdx, rdy = 51, 51, -1,-1,
    #y,x 길이
    n, m = len(wallpaper), len(wallpaper[0])
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                lux = min(lux, j)
                luy = min(luy, i)
                rdx = max(rdx, j)
                rdy = max(rdy, i)
        
    return [luy, lux, rdy+1, rdx+1]