import sys
sys.stdin = open('input.txt')
import itertools

heights = [int(input()) for _ in range(9)]

for i in itertools.combinations(heights, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break