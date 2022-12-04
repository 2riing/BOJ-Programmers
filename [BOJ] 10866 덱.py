import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(sys.stdin.readline().rstrip())
q = deque()

for _ in range(N):
    instruction = sys.stdin.readline().rstrip()
    if instruction[:4] == 'push':
        word, num = instruction.split()
        if word == 'push_front':
            q.appendleft(int(num))
        elif word == 'push_back':
            q.append(int(num))
    elif instruction == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif instruction == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif instruction == 'size':
        print(len(q))
    elif instruction == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif instruction == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif instruction == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])



