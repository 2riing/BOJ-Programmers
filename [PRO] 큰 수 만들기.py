def solution(number, k):
    answer = ''
    stack = []
    
    # stack에 존재하고, 현재 수보다 작고, k만큼 안돌았을 때 pop 한다
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # k만큼 제거하지 못한경우 뒤에서 k개만큼 제거
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)
