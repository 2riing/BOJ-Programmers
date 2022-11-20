import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print((a ** b)%10)
