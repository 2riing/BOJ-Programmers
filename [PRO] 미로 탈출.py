from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    start, lever, end = [],[],[]
    # Start, Lever, End 지점 찾기 
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start = [i, j]
            if maps[i][j] == 'E':
                end = [i, j]
            if maps[i][j] == 'L':
                lever = [i, j]
            
    def BFS(x, y, x1, y1):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
        q = deque()
        q.append([x, y, 0])
        while q:
            row, col, cnt = q.popleft()
            if row == x1 and col == y1: 
                print('레버', row, col, cnt)
                return cnt
            for i in range(4):
                ni, nj = row + di[i], col + dj[i]
                if 0 <= ni < N and 0 <= nj < M:
                    if maps[ni][nj] != 'X' and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        q.append([ni, nj, cnt + 1])
                        
    result1 = BFS(start[0], start[1], lever[0], lever[1])
    result2 = BFS(lever[0], lever[1], end[0], end[1])
    if result1 and result2:
        return result1 + result2
    else: 
        return -1
