import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    temp = input()
    print(temp[0], end='')
    print(temp[-1])
