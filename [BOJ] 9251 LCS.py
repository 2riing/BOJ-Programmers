import sys
sys.stdin = open('input.txt')

one = input()
two = input()

N = len(one)

for i in range(N, 0, -1):
    print(i)