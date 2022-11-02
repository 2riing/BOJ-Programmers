import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())
numbers = []
for _ in range(N):
    temp = int(input())
    numbers.append(temp)

numbers.sort(reverse=True)
answer = []
i = 1
for number in numbers:
    answer.append(number * i)
    i += 1
print(max(answer))