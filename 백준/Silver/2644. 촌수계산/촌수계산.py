n = int(input())
a,b = map(int, input().split()) #두 사이의 관계 
m = int(input())
graph = [[] for _ in range(n+1)]
chk = [False] * (n+1)
result = []

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v,cnt):
    chk[v] = True
    cnt += 1 

    if v == b:
        result.append(cnt)
        
    for k in graph[v]:
        if chk[k] == False:
            dfs(k, cnt)


dfs(a,0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)