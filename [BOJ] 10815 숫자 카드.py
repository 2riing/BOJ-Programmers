import sys
sys.stdin = open('input.txt')

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

cards = set(cards)

ans = []
for number in numbers:
    if number in cards:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)