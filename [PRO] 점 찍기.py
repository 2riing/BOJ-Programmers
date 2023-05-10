def solution(k, d):
    cnt = 0
    for i in range(0, d + 1, k):
        y = int((d*d - i*i) ** (1/2)) // k
        cnt += (y + 1)
    return cnt
