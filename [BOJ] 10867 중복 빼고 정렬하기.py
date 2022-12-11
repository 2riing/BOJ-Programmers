import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
set_nums = list(set(nums))
set_nums.sort()
print(*set_nums)