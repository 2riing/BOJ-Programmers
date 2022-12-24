import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    nums = list(map(int, input().split()))
    nums.sort()
    new_nums = nums[1:-1]
    if new_nums[-1] - new_nums[0] >= 4:
        print('KIN')
    else:
        print(sum(new_nums))
