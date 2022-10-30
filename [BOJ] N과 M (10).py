import sys
sys.stdin = open('input.txt')

def DFS(start):
    global prev
    if len(arr) == M:
        if arr != prev:
            prev = arr[:]
            print(*arr)

            return
    for i in range(start, len(numbers)):
        if len(arr) == 0 or (len(arr) > 0 and numbers[i] >= arr[-1]):
            arr.append(numbers[i])
            DFS(i + 1)
            arr.pop()

N, M = map(int, input().split())
numbers = list(list(map(int, input().split())))
numbers.sort()
arr=[]
prev = []
visited= []
DFS(0)
