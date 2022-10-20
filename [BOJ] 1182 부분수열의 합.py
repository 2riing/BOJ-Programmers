import sys
sys.stdin = open('input.txt')

def DFS(start):
    global cnt
    if sum(arr) == S and len(arr) > 0:
        cnt += 1


    for i in range(start, N):
        arr.append(numbers[i])
        DFS(i + 1)
        arr.pop()

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
arr=[]
DFS(0)
print(cnt)