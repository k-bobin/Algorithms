from collections import deque
def solution(x, y, n):
   
    chk =[-1] * (y+1)
    def bfs(x):
        q = deque()
        q.append(x)
        
        while q:
            x = q.popleft()
            if x == y:
                return chk[y]
            for k in (x+n, x*2, x*3):
                if k <=y:
                    if chk[k] == -1:
                        chk[k] = chk[x] +1
                        q.append(k)
                    
    chk[x] = 0
    t = bfs(x)
    if t is None:
        return -1
    else:
        return t
