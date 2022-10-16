import sys
sys.stdin = open('input.txt')

def DFS():
  if len(arr) == M:
    print(*arr)
    return 
  for i in range(N):
    if numbers[i] not in arr:
      arr.append(numbers[i])
      DFS()
      arr.pop()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
arr=[]
DFS()
