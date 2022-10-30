import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS():
    global beer
    q = deque()
    q.append(home)
    while q:
        row, col = q.popleft()
        if [row, col] == store:
            visited[row][col] = 1
            beer += 20
        if [row, col] == festival:
            return
        for i in range(4):
            di, dj = row + dx[i],  col + dy[i]
            if 0 <= di < festival[0] and 0 <= dj < festival[1]:
                if visited[di][dj] == 0:
                    q.append([di, dj])
                    visited[di][dj] = 1



t = int(input())
for _ in range(t):
    n = int(input()) # 맥주를 파는 편의점의 개수
    home = list(map(int, input().split()))
    store = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        store.append(temp)
    festival = list(map(int, input().split()))
    beer = 20

    visited = [[0 for _ in range(festival[0])] for _ in range(festival[1])]

    dx, dy = [50, -50, 0, 0], [0, 0, 50, -50]

    BFS()