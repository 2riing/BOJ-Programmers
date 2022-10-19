import sys
sys.stdin = open('input.txt')

def DFS():
    if len(arr) == M:
        if tuple(arr) not in visited:
            visited.add(tuple(arr))
            print(*arr)
            return
        else:
            return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            arr.append(numbers[i])
            DFS()
            used[i] = 0
            arr.pop()



N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
used = [0 for _ in range(N)]
visited = set()
prev = []

arr= []
DFS()