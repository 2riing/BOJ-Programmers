import sys
sys.stdin = open('input.txt')

N = int(input())
dp = [1 for i in range(N)]
numbers = list(map(int, input().split()))

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))