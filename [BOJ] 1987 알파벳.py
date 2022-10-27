import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def DFS(row, col, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        di, dj = row + dx[i], col + dy[i]
        if 0 <= di < R and 0 <= dj < C:
            if board[di][dj] not in used:
                used.add(board[di][dj])
                DFS(di, dj, cnt + 1)
                used.remove(board[di][dj])



R, C = map(int, input().split())
board = [input() for _ in range(R)]
answer = 0


used = {board[0][0]}
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

DFS(0, 0, 0)

print(answer + 1)

