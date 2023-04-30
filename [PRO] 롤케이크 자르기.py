# 롤케이크 동일한 가짓수의 토핑을 먹을 수 있다면 공평한 것

def solution(topping):
    answer = 0
    N = len(topping)
    for i in range(1, N):
        left = topping[:i]
        right = topping[i:]
        if len(set(left)) == len(set(right)):
            answer += 1
    return answer
