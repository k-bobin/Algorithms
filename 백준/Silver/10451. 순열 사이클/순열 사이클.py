import sys
sys.setrecursionlimit(10000)
from collections import deque
def solution():
    #graph 만들기 
    n = int(input())
    test = list(map(int,input().split()))
    _list= [[i] for i in range(n+1)]
    chk = [False] * (n+1)
    cnt = 0

    for t in range(len(test)):
        _list[t+1].append(test[t])



    def dfs(num):
        chk[num] = True
        next = _list[num][1]
        if chk[next] == False:
            dfs(next)
        return 



    for i in range(1,len(_list)):
        if chk[i] == False:
            dfs(i)
            cnt +=1 

    print(cnt)
               

T = int(input())
for _ in range(T):
    solution()

    