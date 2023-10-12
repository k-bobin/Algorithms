def solution(n):
    dp = [0] * 5001
    dp[0] = 0
    dp[1] = 3
    dp[2] =11
    
    index = int(n/2)
    if n % 2 != 0:
        return 0
    if index < 3:
        return dp[index]

    for i in range(3, index+1):
        dp[i] = (3*dp[i-1]+ sum(dp[1:i-1])*2+2)%1000000007

    return dp[index]

# 세로가 3일때   2일때
# dp[0] = 0  dp[0] = 0
# dp[1] = 0  dp[1] = 1
# dp[2] = 3  dp[2] = 2
# dp[3] = 0  dp[3] = 3
# dp[4] = 11 dp[4] = 5
# dp[5] = 0  dp[5] = 8
# dp[6] = 41 dp[6] = 13
# dp[7] = 0  dp[7] = 21
#dp[8] =153  dp[8]= 21
123 