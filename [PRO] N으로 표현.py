def solution(N, number):
    # 1개 ~ 8개 사용하는 dp 배열 
    dp = [set() for _ in range(9)]  

    for i in range(1, 9):
        dp[i].add(int(str(N) * i)) # 연속되는 N을 추가
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a + b)
                    dp[i].add(a * b)
                    if a > b:
                        dp[i].add(a - b)
                    elif a < b:
                        dp[i].add(b - a)
                    if a != 0:
                        dp[i].add(b // a)
                    elif b!= 0:
                        dp[i].add(a // b)
        if number in dp[i]:
            return i
    return -1
