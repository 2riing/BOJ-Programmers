def solution(s):
    maxNum = 1
    N = len(s)
    if N == 1: return 1
    else:
        for i in range(N):
            for j in range(N-i-1):
                str = s[i:N-j]
                if str == str[::-1]:
                    if maxNum < len(str):
                        maxNum = len(str)
    return maxNum
