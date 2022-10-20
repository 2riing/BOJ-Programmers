import sys
sys.stdin = open('input.txt')

def DFS(start):
    if len(arr) == 6:
        print(*arr)
        return
    for i in range(start, k):
        arr.append(S[i])
        DFS(i + 1)
        arr.pop()

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break
    else:
        k = numbers[0]
        S = numbers[1:]

    arr = []
    DFS(0)
    print()