import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dp = [[0,0] for _ in range(41)]
    dp[0] = [1,0]
    dp[1] = [0,1]
    dp[2] = [1,1] #a,b  a=dp[i-1][0]+dp[i-2][0], b=dp[i-1][0]+dp[i-1][1]

    if n< 3:
        print(*dp[n])
    else:
        for i in range(3,n+1):
            dp[i][0]= dp[i-1][0]+ dp[i-2][0]
            dp[i][1]=dp[i-1][0]+dp[i-1][1]
        print(*dp[n])
