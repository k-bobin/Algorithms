import sys

sys.setrecursionlimit(10**6)

times = int(input())
for _ in range(times):
    n = int(input())
    _list = [0] + list(map(int, input().split()))
    answer = set()

    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            stack = []
            while not visited[i]:
                stack.append(i)
                visited[i] = True
                i = _list[i]

            if i in stack:
                answer.update(stack[stack.index(i):])

    print(n - len(answer))