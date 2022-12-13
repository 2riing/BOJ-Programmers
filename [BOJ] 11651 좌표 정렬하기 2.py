import sys
sys.stdin = open('input.txt')

points = []

N = int(input())
for _ in range(N):
    point = list(map(int, input().split()))
    points.append(point)

points.sort(key= lambda x : (x[1], x[0]))

for point in points:
    print(*point)