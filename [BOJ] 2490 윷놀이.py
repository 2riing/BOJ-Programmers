import sys
sys.stdin = open('input.txt')

for _ in range(3):
    numbers = list(map(int, input().split()))
    total = sum(numbers)
    if total == 3:
        print('A')
    elif total == 2:
        print('B')
    elif total == 1:
        print('C')
    elif total == 0:
        print('D')
    elif total == 4:
        print('E')