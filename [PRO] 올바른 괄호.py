def solution(s):
    stack = []
    for i in range(len(s)):
        if stack:
            if s[i] == '(': stack.append('(')
            else:
                if stack[-1] == '(': stack.pop()
                else: stack.append('(')
        else: stack.append(s[i])        
    
    if stack: return False
    else: return True
