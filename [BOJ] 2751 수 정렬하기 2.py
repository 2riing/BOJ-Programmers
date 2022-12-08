import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    a = int(input())
    nums.append(a)

nums.sort()
for num in nums:
    print(num)