import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
N, M = map(int, input().split())

numbers = []
for _ in range(N):
    temp = list(map(int, input().split()))
    numbers.append(temp)

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    total = 0
    for k1 in range(i-1, x):
        for k2 in range(j-1, y):
            total += numbers[k1][k2]
    print(total)