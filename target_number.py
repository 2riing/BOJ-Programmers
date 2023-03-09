
def solution(numbers, target): # 사용할 수 있는 숫자, 타겟 넘버 
    answer = 0
    n = len(numbers)
    def DFS(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return 
        else:
            DFS(idx + 1, result + numbers[idx])
            DFS(idx + 1, result - numbers[idx])
    DFS(0, 0)
    return answer
