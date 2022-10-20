import sys
sys.stdin = open('input.txt')

def DFS():
    if len(arr) == N:
        print(*arr)
        return
    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            DFS()
            arr.pop()


N = int(input())
arr = []
DFS()
