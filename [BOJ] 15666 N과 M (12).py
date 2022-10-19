import sys
sys.stdin = open('input.txt')

def DFS():
    if len(arr) == M:
        if tuple(arr) not in used:
            print(*arr)
            used.add(tuple(arr))
            return
        else:
            return
    for i in range(N):
        if len(arr) == 0 or (len(arr) > 0 and arr[-1] <= numbers[i]):
            arr.append(numbers[i])
            DFS()
            arr.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

used = set()
arr = []
DFS()