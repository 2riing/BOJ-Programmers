

N = int(input())
divisers = list(map(int, input().split()))
answer = -1

if len(divisers) > 1:
    divisers.sort()
    answer = divisers[0] * divisers[-1]
else:
    answer = divisers[0]  * divisers[0]

print(answer)
