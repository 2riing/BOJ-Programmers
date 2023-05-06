def solution(sticker):
    if len(sticker) == 1: return sticker[0]

    N = len(sticker)
    dp = [0 for _ in range(N)]
    dp2 = [0 for _ in range(N)]
    dp[0], dp[1] = sticker[0], sticker[0]
                                        
    # 첫번째 스티커 뜯을 때
    for i in range(2, N - 1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    
    for i in range(1, len(sticker)):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])
    return max(dp[-2], dp2[-1])
