import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

jewelry = [list(map(int, input().split())) for _ in range(N)]
C = [int(input()) for _ in range(K)]

print(jewelry, C)
