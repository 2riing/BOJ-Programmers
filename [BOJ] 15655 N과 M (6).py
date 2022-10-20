import sys
sys.stdin = open('input.txt')

def DFS(start, ):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(start, N):
        arr.append(numbers[i])
        DFS(i + 1)
        arr.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
arr = []
DFS(0)