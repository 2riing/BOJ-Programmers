# 0, 1로 채워진 board/ 1칸 1by1
# 1로 이루어진 가장 큰 정사각형을 찾아서 return 재귀..?
# 가로세로 1000, 1000
# 검색결과 dp임

def solution(board):
    answer = 0
    N, M = len(board), len(board[0])
    
    # dp initialize 
    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0] = board[0]
    for i in range(N):
        dp[i][0] = board[i][0]
    
    # dp
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # maxNum
    maxNum = 0
    for i in range(N):
        if max(dp[i]) > maxNum:
            maxNum = max(dp[i])
    
    # answer
    answer = maxNum * maxNum
    return answer
