import sys
sys.stdin = open('input.txt')

def isAvailable(x):
    for i in range(x):
        if pan[x] == pan[i] or abs(pan[x] - pan[i]) == abs(x-i):
            return False
    return True

def N_queens(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        pan[x] = i
        if isAvailable(x): # 이게 가능하다면 !
            N_queens(x + 1)

N = int(input())
pan = [0] * N
cnt = 0
N_queens(0)
print(cnt)