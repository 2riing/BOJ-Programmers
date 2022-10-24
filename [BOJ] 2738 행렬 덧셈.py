import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    temp = []
    for j in range(M):
        temp.append(A[i][j] + B[i][j])
    print(*temp)