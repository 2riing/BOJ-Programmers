import math

def solution(n, k):
    r = k-1
    answer = []
    nums = list(range(1, n+1))
    for i in range(1, n+1):
        print(r, math.factorial(n-i), n-i)
        q, r = divmod(r, math.factorial(n-i)) # 몫. 나머지
        answer.append(nums.pop(q))
    return answer
