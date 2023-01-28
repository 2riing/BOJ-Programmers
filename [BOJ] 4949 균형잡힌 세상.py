import sys
sys.stdin = open('input.txt')

while True:
    words = input()
    if words == '.':
        break
    stack = []
    flag = 1
    for word in words:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if not stack or stack[-1] == '[':
                flag = 0
                break
            elif stack[-1] == '(':
                stack.pop()
        elif word == ']':
            if not stack or stack[-1] == '(':
                flag = 0
                break
            elif stack[-1] == '[':
                stack.pop()


    if flag == 1 and not stack:
        print("yes")
    else:
        print("no")
