import sys
sys.stdin = open('input.txt')

S = int(input())
total = 0
N = 0
for i in range(1, S + 1):
    total += i
    N += 1
    if total > S:
        N-=1
        break
print(N)