#6:24

def solution(m, n, puddles):
    MOD = 1000000007
    _list = [[0] * m for _ in range(n)]
    chk = [[0] * m for _ in range(n)]

    for i, j in puddles:
        _list[j - 1][i - 1] = -1  
    chk[0][0] = 1  

    for i in range(n):
        for j in range(m):
            if _list[i][j] == -1:
                continue

            if i > 0:
                chk[i][j] += chk[i - 1][j] % MOD
            if j > 0:
                chk[i][j] += chk[i][j - 1] % MOD

    answer = chk[n - 1][m - 1] % MOD
    return answer