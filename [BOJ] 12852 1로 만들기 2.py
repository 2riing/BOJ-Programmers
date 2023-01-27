import sys
from collections import deque
sys.stdin = open('input.txt')

# X가 3으로 나누어 떨어지면 3으로 나눈다
# 2로 나누넝떨어지면 2로 나눔
# 1을 뺌
# 이거 모두를 해서 1을 만드려고함 연산 횟수 최소값

def BFS(N):
    q = deque()
    q.append((N, 0, []))
    while q:
        x, cnt, history = q.popleft()
        if x == 1:
            return cnt, history
        dx = [x // 3, x // 2, x - 1]
        for i in range(3):
            if (i == 0 and x % 3 != 0) or (i == 1 and x % 2 != 0):
                pass
            else:
                nx = dx[i]
                if nx not in visited:
                    visited.add(nx)
                    q.append((nx, cnt + 1, [*history, nx] ))


visited = set()
N = int(input())
answer = BFS(N)
print(answer[0])
print(N, *answer[1])


