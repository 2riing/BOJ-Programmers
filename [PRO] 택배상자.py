def solution(order):
    stack = []
    cnt = 0
    i = 1
    while i != len(order) + 1:
        stack.append(i)
        while stack and stack[-1] == order[cnt]:
            cnt += 1
            stack.pop()
        i += 1
    return cnt
