def solution(s):
    answer = ''
    N = len(s)
    if N % 2 == 0: # 짝수면
        answer += s[(N//2 - 1) : (N//2) + 1]
    else: # 홀수면
        answer += s[(N//2) : (N//2) + 1]
    return answer
