import sys
import heapq

N = int(sys.stdin.readline())

times = []
for _ in range(N):
    S, F = map(int, sys.stdin.readline().split())
    heapq.heappush(times, (F, S))

cnt, end = 0, 0
while times:
    if times[0][1] >= end:
        end = heapq.heappop(times)[0]
        cnt += 1
        continue
    heapq.heappop(times)

print(cnt)
