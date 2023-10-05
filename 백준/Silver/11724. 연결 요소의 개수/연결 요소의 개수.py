import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 함수
def dfs(v):
    chk[v] = True
    for i in graph[v]:
        if chk[i] == False:
            dfs(i)

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
chk = [False] * (n+1)

count = 0 # 연결 노드의 수
for i in range(1, n+1):
    if chk[i] == False:
        dfs(i)
        count += 1 # dfs 한 번 끝날 때마다 count+1

print(count)