def solution(land):
    N = len(land)
    dp = [[0 for _ in range(4)] for _ in range(N)]
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, N):
        for j in range(4):
            temps = [0, 1, 2, 3]
            temps.remove(j)
            dp[i][j] = land[i][j] + max(dp[i-1][temps[0]], dp[i-1][temps[1]], dp[i-1][temps[2]])

    return max(dp[-1])
