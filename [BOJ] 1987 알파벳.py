import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def DFS(row, col, cnt):
    global answer
    answer = max(answer, cnt)
    used.add(board[row][col])
    for i in range(4):
        di, dj = row + dx[i], col + dy[i]
        if 0 <= di < R and 0 <= dj < C:
            if board[di][dj] not in used:
                DFS(di, dj, cnt + 1)
    used.remove(board[row][col])



R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
answer = 0
used = set()
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

DFS(0, 0, 1)

print(answer)

