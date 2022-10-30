import sys
sys.stdin = open('input.txt')

def DFS(row, col, M):
    if mint[row][col] == 2:
        M += H
    if M == 0:
        return

    for i in range(4):
        if mint[di][dj] == 0:
            visited[di][dj] = 1
            DFS(di, dj, M - 1)
            visited[di][dj] = 0



N, M, H = map(int, input().split()) # 마을크기, 초기 체력, 증가하는 체력
mint = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if mint[i][j] == 1:
            start_row, start_col = i, j
            visited[i][j] = 1
            break

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
DFS(start_row, start_col, M)
print(visited)
